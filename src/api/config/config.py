from pydantic_settings import BaseSettings

from .logging import Settings as LoggingSettings


class Settings(BaseSettings):
    # Application settings
    app_name: str
    api_port: int
    host: str
    app_run_name: str
    origins: list[str]
    logging: LoggingSettings = LoggingSettings()


settings = Settings()  # type: ignore
