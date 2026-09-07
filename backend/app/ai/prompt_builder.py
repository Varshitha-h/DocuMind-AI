from typing import Dict, List

from app.ai.prompts.base import BASE_SYSTEM_PROMPT
from app.ai.prompts.tasks import TASK_PROMPTS
from app.ai.prompts.documents import DOCUMENT_PROMPTS

from app.ai.task_detector import TaskDetector
from app.ai.document_detector import DocumentDetector


class PromptBuilder:

    def __init__(self):

        self.task_detector = TaskDetector()
        self.document_detector = DocumentDetector()

    def build_prompt(
        self,
        question: str,
        context: str,
        conversation: List[Dict[str, str]]
    ) -> str:

        task = self.task_detector.detect(question)

        document_type = self.document_detector.detect(context)

        task_instruction = self._get_task_instruction(
            task.value
        )

        document_instruction = self._get_document_instruction(
            document_type.value
        )

        conversation_text = self._format_conversation(
            conversation
        )

        cleaned_context = self._clean_context(
            context
        )

        return self._build_prompt(
            question=question,
            task=task.value,
            document=document_type.value,
            task_instruction=task_instruction,
            document_instruction=document_instruction,
            context=cleaned_context,
            conversation=conversation_text
        )
    def _get_task_instruction(
        self,
        task: str
    ) -> str:
        """
        Returns the prompt for the detected task.
        """

        return TASK_PROMPTS.get(
            task,
            TASK_PROMPTS["chat"]
        )


    def _get_document_instruction(
        self,
        document_type: str
    ) -> str:
        """
        Returns the prompt for the detected document type.
        """

        return DOCUMENT_PROMPTS.get(
            document_type,
            DOCUMENT_PROMPTS["general"]
        )


    def _format_conversation(
        self,
        conversation: List[Dict[str, str]]
    ) -> str:
        """
        Formats previous conversation history.
        """

        if not conversation:
            return "No previous conversation."

        history = []

        for message in conversation:

            role = message.get(
                "role",
                "user"
            ).capitalize()

            content = message.get(
                "content",
                ""
            ).strip()

            if content:

                history.append(
                    f"{role}: {content}"
                )

        return "\n".join(history)
    def _clean_context(
        self,
        context: str
    ) -> str:
        """
        Cleans the retrieved RAG context.
        """

        if not context:
            return "No relevant document context was found."

        context = context.strip()

        context = context.replace("\t", " ")

        while "  " in context:
            context = context.replace("  ", " ")

        return context


    def _build_prompt(
        self,
        question: str,
        task: str,
        document: str,
        task_instruction: str,
        document_instruction: str,
        context: str,
        conversation: str
    ) -> str:
        """
        Creates the final prompt sent to the LLM.
        """

        return f"""
{BASE_SYSTEM_PROMPT}

==================================================
DOCUMENT TYPE
==================================================

{document.upper()}

==================================================
USER TASK
==================================================

{task.upper()}

==================================================
TASK INSTRUCTION
==================================================

{task_instruction}

==================================================
DOCUMENT INSTRUCTION
==================================================

{document_instruction}

==================================================
DOCUMENT CONTEXT
==================================================

{context}

==================================================
CONVERSATION HISTORY
==================================================

{conversation}

==================================================
USER QUESTION
==================================================

{question}

==================================================
IMPORTANT RULES
==================================================

1. Answer ONLY the user's question.

2. Use the uploaded document as the primary source.

3. If the answer is available in the document,
do not use outside knowledge.

4. If the answer is not available,
clearly state that before using general knowledge.

5. Never invent facts.

6. Keep responses concise and professional.

7. Use headings or bullet points only when they improve readability.

8. Maintain conversation context for follow-up questions.

9. If asked to summarize, summarize.

10. If asked to recommend, recommend based on the document.

==================================================
FINAL ANSWER
==================================================
"""