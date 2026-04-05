from enum import Enum


class AgentRole(Enum):
    ORCHESTRATOR = "orchestrator"   # 全体を制御するエージェント
    RESEARCHER = "researcher"       # 調査担当
    SUMMARIZER = "summarizer"       # 要約担当
    GENERAL = "general"             # 汎用
