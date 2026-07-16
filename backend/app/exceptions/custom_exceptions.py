from fastapi import HTTPException


class DocumentNotUploadedException(HTTPException):
    """
    Raised when the user asks a question
    before uploading a document.
    """

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Please upload a PDF before asking questions."
        )


class InvalidPDFException(HTTPException):
    """
    Raised when the uploaded file is not a PDF.
    """

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Only PDF files are allowed."
        )


class EmptyDocumentException(HTTPException):
    """
    Raised when no text can be extracted.
    """

    def __init__(self):
        super().__init__(
            status_code=400,
            detail="No readable text found in the uploaded PDF."
        )