import logging

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_dir: str = Field(default="/var/log/seecore_ai", env="LOG_DIR")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    request_log_level: str = Field(default="INFO", env="REQUEST_LOG_LEVEL")

    def get_log_level(self, level_name: str) -> int:
        log_levels = {"DEBUG": logging.DEBUG, "INFO": logging.INFO, "WARNING": logging.WARNING, "ERROR": logging.ERROR, "CRITICAL": logging.CRITICAL}
        return log_levels.get(level_name.upper(), logging.INFO)

    @property
    def parsed_log_level(self) -> int:
        return self.get_log_level(self.log_level)

    @property
    def parsed_request_log_level(self) -> int:
        return self.get_log_level(self.request_log_level)


settings = Settings()
