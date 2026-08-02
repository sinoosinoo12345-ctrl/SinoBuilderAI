from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "{project}"

    VERSION: str = "1.0.0"

    DEBUG: bool = False

    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str

    CORS_ORIGINS: list[str] = [
        "*"
    ]

    class Config:

        env_file = ".env"

        extra = "ignore"


settings = Settings()
