from dataclasses import dataclass


@dataclass
class DocumentChunk:
    """
    Represents one chunk of a document
    along with its metadata.
    """

    chunk_id: int
    page: int
    text: str