import ollama


class LLMService:
    """
    Handles communication with the local Ollama LLM.
    """

    def __init__(self, model_name: str = "llama3.2"):
        """
        Initialize the LLM service.

        Args:
            model_name: Ollama model to use.
        """
        self.model_name = model_name

    def generate_answer(
        self,
        question: str,
        context: str
    ) -> str:
        """
        Generate an answer using the retrieved document context.
        """

        prompt = f"""
You are DocuMind AI.

You are a helpful AI assistant.

Answer the user's question ONLY using the provided document context.

If the answer is not available in the document, reply exactly with:

"I couldn't find that information in the uploaded document."

-----------------------------
Document Context

{context}

-----------------------------
Question

{question}

-----------------------------
Answer
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]