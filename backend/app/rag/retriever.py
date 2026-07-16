from app.config import settings
from app.exceptions.custom_exceptions import DocumentNotUploadedException
from app.rag.embeddings import generate_embeddings
from app.rag.storage import get_vector_store


class Retriever:
    """
    Retrieves the most relevant document chunks
    from the shared FAISS vector store.
    """

    def retrieve(
        self,
        question: str,
        top_k: int | None = None
    ) -> str:
        """
        Retrieve the most relevant chunks for
        the user's question.

        Args:
            question: User's question.
            top_k: Number of chunks to retrieve.

        Returns:
            Combined context string.
        """

        # Use default TOP_K from config
        if top_k is None:
            top_k = settings.TOP_K

        # Get shared vector store
        vector_store = get_vector_store()

        if vector_store is None:
            raise DocumentNotUploadedException()

        # Generate embedding for question
        query_embedding = generate_embeddings(
            [question]
        )[0]

        # Search vector store
        results = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        # Merge retrieved chunks
        context = "\n\n".join(results)

        return context