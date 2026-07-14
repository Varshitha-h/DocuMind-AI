from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

from app.services.pdf_service import save_pdf
from app.services.pdf_reader import extract_text_from_pdf

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF, save it and extract its text.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Save PDF
    result = save_pdf(file)

    # Build file path
    file_path = Path("uploads") / result["stored_filename"]

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    print("\n========== Extracted PDF Text ==========\n")
    print(extracted_text[:500])
    print("\n========================================\n")

    return {
        "message": "PDF uploaded successfully.",
        "original_filename": result["original_filename"],
        "stored_filename": result["stored_filename"],
        "preview": extracted_text[:500]
    }