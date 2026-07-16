from pathlib import Path

from fastapi import HTTPException, UploadFile

from app.services.pdf_service import save_pdf
from app.services.pdf_reader import extract_text_from_pdf

from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings

from app.rag.storage import initialize_vector_store


class DocumentPipeline:
    """
    Handles the complete document ingestion pipeline.

    Steps:
        1. Save PDF
        2. Extract text
        3. Split into chunks
        4. Generate embeddings
        5. Store vectors in FAISS
    """

    def process_document(
        self,
        file: UploadFile
    ) -> dict:
        """
        Process an uploaded PDF.

        Args:
            file: Uploaded PDF file.

        Returns:
            Dictionary containing processing details.
        """

        # ----------------------------
        # Validate File
        # ----------------------------
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

        # ----------------------------
        # Save PDF
        # ----------------------------
        result = save_pdf(file)

        file_path = Path("uploads") / result["stored_filename"]

        # ----------------------------
        # Extract Text
        # ----------------------------
        extracted_text = extract_text_from_pdf(file_path)

        # ----------------------------
        # Split into Chunks
        # ----------------------------
        chunks = chunk_text(extracted_text)

        # ----------------------------
        # Generate Embeddings
        # ----------------------------
        embeddings = generate_embeddings(chunks)

        # ----------------------------
        # Initialize Shared Vector Store
        # ----------------------------
        vector_store = initialize_vector_store(
            len(embeddings[0])
        )

        # ----------------------------
        # Store Embeddings
        # ----------------------------
        vector_store.add_embeddings(
            embeddings=embeddings,
            chunks=chunks
        )

        return {
            "message": "Document processed successfully.",
            "original_filename": result["original_filename"],
            "stored_filename": result["stored_filename"],
            "total_chunks": len(chunks),
            "embedding_dimension": len(embeddings[0]),
            "vectors_stored": vector_store.index.ntotal
        }