from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Message:
    role: str  # "user" | "assistant" | "tool"
    content: str
    created_at: datetime = field(default_factory=datetime.utcnow)

    def is_from_user(self) -> bool:
        return self.role == "user"

    def is_from_assistant(self) -> bool:
        return self.role == "assistant"

    def is_tool_result(self) -> bool:
        return self.role == "tool"
