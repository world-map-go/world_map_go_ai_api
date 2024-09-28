# world_map_go_ai_api

## start guide

```
# クローン
git clone git@github.com:world-map-go/world_map_go_ai_api.git

# ディレクトリの移動
cd world_map_go_ai_api

# .env の記述
echo "PROJECT_NAME=FastAPI Clean Architecture Example" >> .env
echo "VERSION=1.0.0" >> .env
```

docker を使う場合
```
# ビルドして起動
docker-compose up --build
```

直接構築の場合
```
# ライブラリのインストール
pip install --no-cache-dir -r requirements.txt

# 起動
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## swagger
開発時は以下リンクにアクセス

http://localhost:8000/docs