from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from src.domain.entities.message import Message
from src.domain.entities.tool_call import ToolCall


@dataclass
class LlmResponse:
    content: str
    tool_calls: list[ToolCall] = field(default_factory=list)

    def has_tool_calls(self) -> bool:
        return len(self.tool_calls) > 0


class LlmClient(ABC):

    @abstractmethod
    def complete(
        self,
        messages: list[Message],
        tools: list[dict],
        system_prompt: str = "",
    ) -> LlmResponse:
        ...
