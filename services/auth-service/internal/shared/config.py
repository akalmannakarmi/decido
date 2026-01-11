from pydantic import BaseSettings


class Settings(BaseSettings):
    service_name: str = "auth-service"
    env: str = "development"

    database_url: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 15
    
    allowed_services: list[str] = [
        "ballot-service",
        "vote-service",
    ]

    class Config:
        env_file = ".env"


settings = Settings()
