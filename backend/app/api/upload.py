from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.rag.chunker import chunk_text
from app.services.pdf_reader import extract_text_from_pdf
from app.services.pdf_service import save_pdf

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, save it, extract text, and split it into chunks.
    """

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save PDF
    result = save_pdf(file)

    # Build path to saved PDF
    file_path = Path("uploads") / result["stored_filename"]

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Create chunks
    chunks = chunk_text(extracted_text)

    # Print chunk information in terminal
    print("\n========== CHUNK INFORMATION ==========\n")
    print(f"Total Chunks Created: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n----------- Chunk {index} -----------")
        print(chunk[:300])

    print("\n======================================\n")

    return {
        "message": "PDF uploaded successfully.",
        "original_filename": result["original_filename"],
        "stored_filename": result["stored_filename"],
        "total_chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else ""
    }