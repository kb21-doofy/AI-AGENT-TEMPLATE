from dataclasses import dataclass


@dataclass(frozen=True)
class LlmConfig:
    provider: str           # "anthropic" | "openai"
    model: str              # "claude-opus-4-6" など
    temperature: float = 0.7
    max_tokens: int = 4096
