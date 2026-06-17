from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    APP_NAME: str = "PyGate"

    DEBUG: bool = True

    ENVIRONMENT: str = "development"

    JWT_SECRET: str = "super-secret-key"

    JWT_ALGORITHM: str = "HS256"

    JWT_EXPIRE_MINUTES: int = 60

    redis_host: str = "localhost"

    redis_port: int = 6379

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore",
        )
    )


settings = Settings()
