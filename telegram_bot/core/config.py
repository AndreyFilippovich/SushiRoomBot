"""Настройки бота."""
from typing import Any, Callable

from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings


def assemble_api_url(system_name: str) -> Callable:
    def validator(v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return AnyHttpUrl.build(
            scheme="http",
            host=values.get(f"{system_name}_host"),
            port=values.get(f"{system_name}_port"),
            path=values.get(f"{system_name}_path"),
        )

    return validator


class Settings(BaseSettings):
    """Настройки бота."""

    token: str = None
    database_host: str
    database_port: int
    database_path: str
    api_url: AnyHttpUrl | None = None

    assemble_api_url = validator("api_url", pre=True, allow_reuse=True)(assemble_api_url("database"))

    class Config:

        env_file = ".env"


settings = Settings()