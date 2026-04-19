---
name: new-agent
description: DDDレイヤーに沿って新しいエージェントの雛形ファイルを生成する
argument-hint: <AgentName> [説明]
allowed-tools: Read Write Glob Bash
---

新しいエージェントをDDDレイヤーに沿って雛形生成する。

## 使い方

```
/new-agent <AgentName> [説明]
```

例: `/new-agent SearchAgent ウェブ検索を行うエージェント`

## 生成するファイル

1. `src/application/ports/<agent_name>_port.py` — ポートインターフェース
2. `src/infrastructure/agents/<agent_name>.py` — インフラ実装
3. `src/application/use_cases/<agent_name>_use_case.py` — ユースケース
4. `src/presentation/routers/<agent_name>_router.py` — FastAPIルーター

## 制約

- domain層は外部ライブラリに依存しない純粋なPythonのみ
- infrastructure層でのみAnthropicやその他外部SDKをimport可能
- 全ファイルに型ヒントを付ける
- dataclassを使用（presentationスキーマはPydantic）

$ARGUMENTS
