from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    log_level: str = "INFO"


def init_settings() -> None:
    global settings
    settings = Settings()


settings = None
if not settings:
    init_settings()
