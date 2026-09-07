from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.models import DocumentChunk


def chunk_text(text: str) -> list[DocumentChunk]:
    """
    Split extracted text into smaller overlapping chunks
    and attach metadata to each chunk.

    Args:
        text: Extracted text from a PDF.

    Returns:
        List of DocumentChunk objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    split_chunks = text_splitter.split_text(text)

    chunks: list[DocumentChunk] = []

    for index, chunk in enumerate(split_chunks, start=1):
        chunks.append(
            DocumentChunk(
                chunk_id=index,
                page=1,          # Temporary (we'll replace with real page numbers later)
                text=chunk
            )
        )

    return chunks