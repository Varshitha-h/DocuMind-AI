from sentence_transformers import SentenceTransformer


# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    """
    Generate embeddings for a list of text chunks.

    Args:
        chunks: List of text chunks.

    Returns:
        List of embedding vectors.
    """

    embeddings = model.encode(chunks)

    return embeddings.tolist()