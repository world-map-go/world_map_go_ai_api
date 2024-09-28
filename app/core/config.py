from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    VERSION: str

    class Config:
        env_file = ".env"  # .env ファイルを指定

# インスタンスを作成して設定を読み込む
settings = Settings()
