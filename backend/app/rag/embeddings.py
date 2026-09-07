from sentence_transformers import SentenceTransformer

from app.rag.models import DocumentChunk


# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding_model():
    """
    Return the loaded embedding model.
    """
    return model


def generate_embeddings(
    chunks: list[DocumentChunk]
) -> list[list[float]]:
    """
    Generate embeddings for a list of document chunks.

    Args:
        chunks: List of DocumentChunk objects.

    Returns:
        List of embedding vectors.
    """

    texts = [chunk.text for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    return embeddings.tolist()