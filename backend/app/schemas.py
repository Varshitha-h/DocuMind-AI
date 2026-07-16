from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Request model for the chat endpoint.
    """

    question: str


class ChatResponse(BaseModel):
    """
    Response model for the chat endpoint.
    """

    question: str
    answer: str
    context: str


class UploadResponse(BaseModel):
    """
    Response model for the upload endpoint.
    """

    message: str
    original_filename: str
    stored_filename: str
    total_chunks: int
    embedding_dimension: int
    vectors_stored: int