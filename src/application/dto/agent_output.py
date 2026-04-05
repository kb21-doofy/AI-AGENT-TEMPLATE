from dataclasses import dataclass


@dataclass
class AgentOutput:
    message: str
    conversation_id: str
