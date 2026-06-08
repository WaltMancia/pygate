from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):

    APP_NAME: str = "PyGate"

    DEBUG: bool = True

    ENVIRONMENT: str = "development"

    model_config = (
        SettingsConfigDict(
            env_file=".env"
        )
    )


settings = Settings()
