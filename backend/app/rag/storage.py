from app.rag.vector_store import VectorStore

# Shared Vector Store instance
vector_store = None


def initialize_vector_store(dimension: int):
    """
    Initialize the shared vector store only once.
    """
    global vector_store

    if vector_store is None:
        vector_store = VectorStore(dimension)

    return vector_store


def get_vector_store():
    """
    Return the shared vector store.
    """
    return vector_store