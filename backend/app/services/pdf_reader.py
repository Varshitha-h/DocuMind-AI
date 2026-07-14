from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(file_path: Path) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Extracted text as a string.
    """

    reader = PdfReader(file_path)

    extracted_text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            extracted_text += page_text + "\n"

    return extracted_text