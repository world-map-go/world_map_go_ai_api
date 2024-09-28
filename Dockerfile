# ベースイメージを指定
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# .env ファイルをコピー
COPY .env .

# アプリケーションのソースコードをコピー
COPY . .

# 起動コマンド (ホットリロードのため `--reload` オプションを指定)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
