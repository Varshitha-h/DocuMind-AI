from app.memory.memory import Message


class MemoryService:
    """
    Stores conversation history.

    Current version:
        - In-memory

    Future:
        - Redis
        - PostgreSQL
        - MongoDB
    """

    def __init__(self):
        self.messages: list[Message] = []

    def add_user_message(self, message: str) -> None:
        self.messages.append(
            Message(
                role="user",
                content=message
            )
        )

    def add_ai_message(self, message: str) -> None:
        self.messages.append(
            Message(
                role="assistant",
                content=message
            )
        )

    def get_history(self) -> list[dict[str, str]]:
        """
        Returns conversation history
        in a format expected by PromptBuilder.
        """
        return [
            {
                "role": message.role,
                "content": message.content
            }
            for message in self.messages
        ]

    def clear(self) -> None:
        self.messages.clear()


_memory_service = MemoryService()


def get_memory_service() -> MemoryService:
    return _memory_service