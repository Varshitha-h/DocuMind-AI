import faiss
import numpy as np


class VectorStore:
    """
    Stores embeddings and their corresponding text chunks using FAISS.
    """

    def __init__(self, dimension: int):
        """
        Initialize the FAISS index and chunk storage.
        """
        self.index = faiss.IndexFlatL2(dimension)

        # Stores the original text chunks
        self.chunks = []

    def add_embeddings(
        self,
        embeddings: list[list[float]],
        chunks: list[str]
    ) -> None:
        """
        Add embeddings and corresponding text chunks.
        """

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3
    ):
        """
        Search the closest matching chunks.
        """

        query = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query, top_k)

        results = []

        for idx in indices[0]:
            if idx != -1:
                results.append(self.chunks[idx])

        return results