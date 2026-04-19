---
name: check
description: mypy・ruff・pytestをまとめて実行してコード品質をチェックする
allowed-tools: Bash
---

コードの品質チェックをまとめて実行する。

## 実行内容

```bash
uv run mypy src/
uv run ruff check src/
uv run pytest tests/ -v
```

エラーがあれば原因と修正方法を日本語で説明する。
