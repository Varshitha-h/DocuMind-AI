from fastapi import APIRouter, File, UploadFile

from app.services.document_pipeline import DocumentPipeline

router = APIRouter()

pipeline = DocumentPipeline()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and process it.
    """

    return pipeline.process_document(file)