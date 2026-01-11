from pydantic import BaseSettings


class Settings(BaseSettings):
    service_name: str = "ballot-service"
    env: str = "development"

    database_url: str

    jwt_secret: str
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()

