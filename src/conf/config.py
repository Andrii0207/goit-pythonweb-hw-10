# class Config:
#     DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/contacts_app"
#
#     JWT_SECRET = "your_secret_key"
#     JWT_ALGORITHM = "HS256"
#     JWT_EXPIRATION_SECONDS = 3600
#
# config = Config


from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600
    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

settings = Settings()

