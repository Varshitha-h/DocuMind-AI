from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import save_pdf
router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file.
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    filename = save_pdf(file)

    return {
        "message": "PDF uploaded successfully.",
        "filename": filename
    }