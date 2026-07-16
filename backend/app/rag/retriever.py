from app.rag.embeddings import generate_embeddings
from app.rag.storage import get_vector_store


class Retriever:
    """
    Retrieves the most relevant document chunks from FAISS.
    """

    def retrieve(
        self,
        question: str,
        top_k: int = 3
    ) -> str:
        """
        Retrieve the most relevant chunks for the user's question.
        """

        # Get shared vector store
        vector_store = get_vector_store()

        if vector_store is None:
            raise Exception(
                "No document has been uploaded yet."
            )

        # Generate embedding for question
        query_embedding = generate_embeddings([question])[0]

        # Search FAISS
        results = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        # Merge chunks into one context
        context = "\n\n".join(results)

        return context