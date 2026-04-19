from dataclasses import dataclass, field
from uuid import uuid4

from app.src.domain.value_objects.agent_role import AgentRole
from app.src.domain.value_objects.llm_config import LlmConfig


@dataclass
class Agent:
    name: str
    role: AgentRole
    llm_config: LlmConfig
    id: str = field(default_factory=lambda: str(uuid4()))
    system_prompt: str = ""

    def is_orchestrator(self) -> bool:
        return self.role == AgentRole.ORCHESTRATOR
