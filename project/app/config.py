import logging
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False
    database_url: AnyUrl


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config setting the environment...")
    return Settings()
