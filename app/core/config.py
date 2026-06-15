from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    APP_NAME: str = "PyGate"

    DEBUG: bool = True

    ENVIRONMENT: str = "development"

    JWT_SECRET: str

    JWT_ALGORITHM: str

    JWT_EXPIRE_MINUTES: int = 60

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore",
        )
    )


settings = Settings()
