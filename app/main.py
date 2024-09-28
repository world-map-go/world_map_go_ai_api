from fastapi import FastAPI
from app.api.v1.hello import router as hello_router
from app.core.config import settings

# settings オブジェクトを使用してアプリ名とバージョンを指定
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# ルーティングを登録
app.include_router(hello_router, prefix="/api/v1")
