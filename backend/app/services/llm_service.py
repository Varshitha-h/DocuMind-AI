import ollama

from app.config import settings
from app.logger import logger


class LLMService:
    """
    Handles communication with the local Ollama LLM.
    """

    def __init__(self):
        """
        Initialize the LLM service.
        """
        self.model_name = settings.LLM_MODEL

    def generate_answer(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Generate an answer using the retrieved document context.

        Args:
            question: User's question.
            context: Retrieved document context.

        Returns:
            AI-generated answer.
        """

        prompt = f"""
You are DocuMind AI.

You are a helpful AI assistant that answers questions ONLY from the provided document.

Instructions:
- Use only the information available in the document context.
- Do not make up information.
- If the answer cannot be found in the document, reply exactly:

"I couldn't find that information in the uploaded document."

----------------------------------------
Document Context

{context}

----------------------------------------
Question

{question}

----------------------------------------
Answer
"""

        logger.info("Generating response using %s...", self.model_name)

        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            logger.info("LLM response generated successfully.")

            return response["message"]["content"]

        except Exception as error:
            logger.exception("LLM generation failed.")

            raise RuntimeError(
                "Failed to generate response from the language model."
            ) from error