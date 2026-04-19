# AI Agent Template

FastAPI + DDDアーキテクチャによるAIエージェント開発のテンプレート。

## 開発環境

プロジェクトルートで `docker-compose up --build` を実行するだけで、**Python・uv・FastAPI** がインストール済みのコンテナが起動し、すぐに開発を始められる。

```bash
docker-compose up --build
```

起動後、[http://localhost:8000/docs](http://localhost:8000/docs) でSwagger UIにアクセスできる。

コードの変更はホットリロードで自動反映される。

## アーキテクチャ

クリーンアーキテクチャ / DDDを採用。依存の方向は `domain → application → infrastructure` の一方向のみ。
