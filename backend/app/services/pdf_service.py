from pathlib import Path
from fastapi import UploadFile
import shutil
import uuid
import logging

# -----------------------------
# Configure Logging
# -----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------
# Upload Directory
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"


def save_pdf(file: UploadFile) -> dict:
    """
    Saves the uploaded PDF to the uploads folder.

    Returns:
        Dictionary containing original filename and stored filename.
    """

    # Create uploads directory if it doesn't exist
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_path = UPLOAD_DIR / unique_filename

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info("Uploaded PDF: %s", unique_filename)

    return {
        "original_filename": file.filename,
        "stored_filename": unique_filename
    }