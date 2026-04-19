---
name: add-tool
description: エージェントが使用するToolPort実装ツールを追加する
argument-hint: <ToolName> [説明]
allowed-tools: Read Write Glob
---

エージェントが使用するツールを追加する。

## 使い方

```
/add-tool <ToolName> [説明]
```

例: `/add-tool WebSearch ウェブ検索ツール`

## 生成するファイル

1. `src/infrastructure/tools/<tool_name>.py` — ToolPort継承の実装クラス

## 実装テンプレート

```python
from src.application.ports.tool_port import ToolPort

class <ToolName>(ToolPort):
    def execute(self, **kwargs) -> dict:
        ...
```

$ARGUMENTS
