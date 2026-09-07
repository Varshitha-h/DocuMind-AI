from app.config import settings
from app.exceptions.custom_exceptions import DocumentNotUploadedException
from app.rag.embeddings import generate_embeddings
from app.rag.models import DocumentChunk
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
            Formatted context string.
        """

        vector_store = get_vector_store()

        if vector_store is None:
            raise DocumentNotUploadedException()

        # ---------------------------------------------
        # Smart Retrieval Strategy
        # ---------------------------------------------

        total_chunks = vector_store.get_total_chunks()

        if top_k is None:

            if total_chunks <= 15:
                top_k = total_chunks

            elif total_chunks <= 50:
                top_k = min(10, total_chunks)

            else:
                top_k = settings.TOP_K

        # ---------------------------------------------

        query_embedding = generate_embeddings(
            [
                DocumentChunk(
                    chunk_id=0,
                    page=0,
                    text=question
                )
            ]
        )[0]

        results: list[DocumentChunk] = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        context_parts = []

        for chunk in results:

            context_parts.append(
                f"""
[Source]
Page: {chunk.page}
Chunk: {chunk.chunk_id}

Content:
{chunk.text}
""".strip()
            )

        return "\n\n-----------------------------\n\n".join(context_parts)