from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.pdf_service import save_pdf
from app.services.pdf_reader import extract_text_from_pdf
from app.rag.chunker import chunk_text
from app.rag.embeddings import generate_embeddings

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, save it, extract text,
    split it into chunks, and generate embeddings.
    """

    # Validate uploaded file
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save PDF
    result = save_pdf(file)

    # Build path to saved PDF
    file_path = Path("uploads") / result["stored_filename"]

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    print("\n========== EXTRACTED TEXT ==========\n")
    print(extracted_text[:500])
    print("\n====================================\n")

    # Split text into chunks
    chunks = chunk_text(extracted_text)

    print("\n========== CHUNK INFORMATION ==========\n")
    print(f"Total Chunks Created: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n----------- Chunk {index} -----------")
        print(chunk[:300])

    print("\n=======================================\n")

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    print("\n========== EMBEDDINGS ==========\n")
    print(f"Total Embeddings: {len(embeddings)}")

    if embeddings:
        print(f"Embedding Dimension: {len(embeddings[0])}")

    print("\n================================\n")

    return {
        "message": "PDF processed successfully.",
        "original_filename": result["original_filename"],
        "stored_filename": result["stored_filename"],
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]) if embeddings else 0,
        "first_chunk": chunks[0] if chunks else ""
    }