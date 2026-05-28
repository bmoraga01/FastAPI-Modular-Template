from pathlib import Path
from typing import Literal
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

# Load env file
if os.path.exists(".env.local"):
    load_dotenv(".env.local", override=True)
else:
    load_dotenv(".env", override=True)


class Settings(BaseSettings):
    APP_ENV: Literal["local", "staging", "prod"]
    APP_ENCRYPTION_KEY: str
    SECRET_KEY: str
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATABASE_URL: str
    ALGORITHM: str
    ACCESS_TOKEN_EXP_MIN: int

    # REDIS
    # REDIS_HOST: str
    # REDIS_PORT: int

    CORS_ORIGINS_URL: str

    REFRESH_TOKEN_EXP_DAYS: int = 7

    ACTIVATION_ATTEMPT_LIMIT: int = 5
    ACTIVATION_BLOCK_SECONDS: int = 600

    model_config = {"env_file_encoding": "utf-8"}


settings = Settings()  # type: ignore
