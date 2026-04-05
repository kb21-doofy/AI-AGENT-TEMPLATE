from abc import ABC, abstractmethod

from src.domain.entities.conversation import Conversation


class ConversationRepository(ABC):

    @abstractmethod
    def save(self, conversation: Conversation) -> None:
        ...

    @abstractmethod
    def find_by_id(self, id: str) -> Conversation | None:
        ...

    @abstractmethod
    def delete(self, id: str) -> None:
        ...

    @abstractmethod
    def find_all(self) -> list[Conversation]:
        ...
