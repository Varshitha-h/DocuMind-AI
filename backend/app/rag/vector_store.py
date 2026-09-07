import faiss
import numpy as np

from app.rag.models import DocumentChunk


class VectorStore:
    """
    Stores document embeddings and metadata using FAISS.
    """

    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

        # Stores DocumentChunk objects
        self.chunks: list[DocumentChunk] = []

    def clear(self) -> None:
        """
        Clears the current document from memory.
        """

        self.index = faiss.IndexFlatL2(self.dimension)
        self.chunks.clear()

    def add_embeddings(
        self,
        embeddings: list[list[float]],
        chunks: list[DocumentChunk]
    ) -> None:
        """
        Store embeddings along with their document chunks.
        """

        self.clear()

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.chunks = chunks.copy()

    def get_total_chunks(self) -> int:
        """
        Returns total chunks stored.
        """

        return len(self.chunks)

    def search(
        self,
        query_embedding: list[float],
        top_k: int
    ) -> list[DocumentChunk]:
        """
        Search the most relevant document chunks.
        """

        if not self.chunks:
            return []

        top_k = min(top_k, len(self.chunks))

        query = np.array([query_embedding]).astype("float32")

        _, indices = self.index.search(query, top_k)

        results: list[DocumentChunk] = []

        for idx in indices[0]:

            if 0 <= idx < len(self.chunks):
                results.append(self.chunks[idx])

        return results