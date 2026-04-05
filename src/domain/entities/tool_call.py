from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class ToolCall:
    tool_name: str
    input: dict
    output: str | None = None
    id: str = field(default_factory=lambda: str(uuid4()))

    def is_completed(self) -> bool:
        return self.output is not None
