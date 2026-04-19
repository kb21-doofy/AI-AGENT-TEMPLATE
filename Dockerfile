FROM python:3.12-slim

# uvのインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# 作業ディレクトリの設定
WORKDIR /app

# uvの環境変数設定
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/.venv/bin:$PATH"

# 依存関係ファイルのコピーとインストール
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-install-project

# アプリケーションコードのコピー
COPY . .
RUN uv sync --no-install-project

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
