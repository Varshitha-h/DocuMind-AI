from pathlib import Path

from fastapi import UploadFile

from app.exceptions.custom_exceptions import (
    EmptyDocumentException,
    InvalidPDFException,
)
from app.logger import logger
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings
from app.rag.storage import initialize_vector_store
from app.services.pdf_reader import extract_text_from_pdf
from app.services.pdf_service import save_pdf


class DocumentPipeline:
    """
    Handles the complete document processing pipeline.

    Workflow:
        1. Validate uploaded file
        2. Save PDF
        3. Extract text
        4. Split text into chunks
        5. Generate embeddings
        6. Store embeddings in the shared FAISS vector store
    """

    def process_document(
        self,
        file: UploadFile
    ) -> dict:
        """
        Process an uploaded PDF document.

        Args:
            file: Uploaded PDF file.

        Returns:
            Dictionary containing document processing information.
        """

        # -------------------------------------------------
        # Validate uploaded file
        # -------------------------------------------------
        if file.content_type != "application/pdf":
            logger.warning("Invalid file uploaded: %s", file.filename)
            raise InvalidPDFException()

        logger.info("Uploading PDF: %s", file.filename)

        # -------------------------------------------------
        # Save PDF
        # -------------------------------------------------
        result = save_pdf(file)

        logger.info(
            "PDF saved successfully: %s",
            result["stored_filename"]
        )

        file_path = Path("uploads") / result["stored_filename"]

        # -------------------------------------------------
        # Extract text
        # -------------------------------------------------
        extracted_text = extract_text_from_pdf(file_path)

        if not extracted_text.strip():
            logger.error(
                "No readable text found in: %s",
                result["stored_filename"]
            )
            raise EmptyDocumentException()

        logger.info("Text extracted successfully.")

        # -------------------------------------------------
        # Split into chunks
        # -------------------------------------------------
        chunks = chunk_text(extracted_text)

        logger.info(
            "Created %d text chunk(s).",
            len(chunks)
        )

        # -------------------------------------------------
        # Generate embeddings
        # -------------------------------------------------
        embeddings = generate_embeddings(chunks)

        logger.info(
            "Generated %d embedding(s).",
            len(embeddings)
        )

        # -------------------------------------------------
        # Initialize shared vector store
        # -------------------------------------------------
        vector_store = initialize_vector_store(
            len(embeddings[0])
        )

        # -------------------------------------------------
        # Store embeddings
        # -------------------------------------------------
        vector_store.add_embeddings(
            embeddings=embeddings,
            chunks=chunks
        )

        logger.info(
            "Vector store updated successfully. Total vectors: %d",
            vector_store.index.ntotal
        )

        return {
            "message": "Document processed successfully.",
            "original_filename": result["original_filename"],
            "stored_filename": result["stored_filename"],
            "total_chunks": len(chunks),
            "embedding_dimension": len(embeddings[0]),
            "vectors_stored": vector_store.index.ntotal
        }