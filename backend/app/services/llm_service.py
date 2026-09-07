from ollama import Client

from app.ai.prompt_builder import PromptBuilder
from app.config import settings
from app.logger import logger
from app.memory.memory_service import get_memory_service


class LLMService:
    """
    Handles communication with the Ollama LLM.
    """

    def __init__(self):
        """
        Initialize the LLM service.
        """

        self.model_name = settings.LLM_MODEL

        self.prompt_builder = PromptBuilder()

        self.memory = get_memory_service()

        self.client = Client(
            host="https://ollama.com",
            headers={
                "Authorization": f"Bearer {settings.OLLAMA_API_KEY}"
            }
        )

    def generate_answer(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Generate an AI response using the uploaded document
        and the user's question.

        Args:
            question: User's question.
            context: Retrieved document context.

        Returns:
            AI-generated answer.
        """

        # Get previous conversation
        conversation_history = self.memory.get_history()

        # Build prompt
        prompt = self.prompt_builder.build_prompt(
            question=question,
            context=context,
            conversation=conversation_history
        )

        logger.info(
            "Generating response using %s...",
            self.model_name
        )

        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response["message"]["content"]

            # Save conversation to memory
            self.memory.add_user_message(question)
            self.memory.add_ai_message(answer)

            logger.info(
                "LLM response generated successfully."
            )

            return answer

        except Exception as error:
            logger.exception(
                "LLM generation failed."
            )

            raise RuntimeError(
                "Failed to generate response from the language model."
            ) from error