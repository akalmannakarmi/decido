from pydantic_settings import BaseSettings
from typing import Annotated, Any

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field,
)



def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",") if i.strip()]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    DEBUG: bool = True
    PROJECT_NAME: str = "decido"

    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALOGRITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10 * 60  # 10 mins
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 30 * 24 * 60 * 60   # 30 days

    
    FRONTEND_HOST: str = "http://localhost:5173"
    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]


    class Config:
        env_file = ".env"


settings = Settings()
