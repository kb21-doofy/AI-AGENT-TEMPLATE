from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class AgentInput:
    message: str
    conversation_id: str = field(default_factory=lambda: str(uuid4()))
    agent_id: str = ""
