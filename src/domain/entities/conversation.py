from dataclasses import dataclass, field
from uuid import uuid4

from src.domain.entities.message import Message


@dataclass
class Conversation:
    id: str = field(default_factory=lambda: str(uuid4()))
    messages: list[Message] = field(default_factory=list)

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def get_messages(self) -> list[Message]:
        return list(self.messages)

    def clear(self) -> None:
        self.messages = []

    def is_empty(self) -> bool:
        return len(self.messages) == 0
