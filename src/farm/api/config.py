from typing import Any, Dict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///src/farm/database/cangrow.db"
    CONNECT_ARGS: Dict[str, Any] = {"check_same_thread": False}

settings = Settings
