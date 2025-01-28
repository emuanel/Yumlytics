from pydantic_settings import BaseSettings

from .logging import Settings as LoggingSettings


class Settings(BaseSettings):
    celery_name: str
    celery_workers: int
    return_mock_parsed_schema: bool

    redis_port: str
    redis_service: str
    flower_service: str

    logging: LoggingSettings = LoggingSettings()

    @property
    def celery_broker_url(self) -> str:
        return f"{self.redis_service}://{self.redis_service}:{self.redis_port}/0"

    @property
    def celery_backend_url(self) -> str:
        return self.celery_broker_url


settings = Settings()
