# AI-AGENT-TEMPLATE

## プロジェクト概要

FastAPI + DDDアーキテクチャによるAIエージェントのテンプレートリポジトリ。
LLMを活用したマルチエージェントシステムの雛形として使用する。

## アーキテクチャ

クリーンアーキテクチャ / DDD（ドメイン駆動設計）を採用。

```
app/
├── main.py          # FastAPIアプリケーションエントリーポイント
└── src/
    ├── domain/          # ビジネスロジックの核心（外部依存なし）
    │   ├── entities/    # エンティティ（Agent, Message, Conversation, ToolCall）
    │   ├── repositories/  # リポジトリインターフェース
    │   └── value_objects/ # 値オブジェクト（AgentRole, LlmConfig）
    ├── application/     # ユースケース層
    │   ├── dto/         # データ転送オブジェクト（AgentInput, AgentOutput）
    │   ├── ports/       # ポートインターフェース（LlmClient, ToolPort）
    │   └── use_cases/   # ユースケース実装
    ├── infrastructure/  # 外部依存の実装
    │   ├── agents/      # エージェント実装
    │   ├── llm/         # LLMクライアント実装
    │   ├── persistence/ # リポジトリ実装
    │   └── tools/       # ツール実装
    └── presentation/    # APIレイヤー
        ├── routers/     # FastAPIルーター
        └── schemas/     # リクエスト/レスポンスのPydanticスキーマ
```

## 技術スタック

- **言語**: Python 3.12+
- **Webフレームワーク**: FastAPI
- **パッケージ管理**: uv
- **コンテナ**: Docker / docker-compose
- **LLM**: Anthropic Claude API（予定）

## 開発ルール

### 依存関係の方向
domain → application → infrastructure の順で依存。逆方向は禁止。

### コーディング規約
- dataclassを積極的に使用する（Pydanticはpresentationのスキーマのみ）
- 型ヒントを必ず付ける
- コメントは「なぜ」が非自明な場合のみ記述

### 新しいエージェントの追加手順
1. `app/src/domain/entities/` にエンティティがなければ追加
2. `app/src/application/ports/` にインターフェース定義
3. `app/src/infrastructure/` に実装
4. `app/src/application/use_cases/` にユースケース
5. `app/src/presentation/routers/` にエンドポイント

## コマンド

```bash
# 開発サーバー起動
uvicorn app.main:app --reload

# Docker起動
docker-compose up

# 依存関係追加
uv add <package>

# 依存関係インストール
uv sync
```

## 注意事項

- APIキーなどのシークレットは `.env` で管理し、コミットしない
- `infrastructure/` 層のみが外部API（Anthropic等）に直接依存してよい
