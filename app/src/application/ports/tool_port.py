from abc import ABC, abstractmethod


class ToolPort(ABC):

    @abstractmethod
    def run(self, input: dict) -> str:
        ...

    @abstractmethod
    def get_definition(self) -> dict:
        """LLMに渡すツール定義を返す"""
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...
