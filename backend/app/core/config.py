import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    MariaDBDsn,
    computed_field,
    AnyUrl,
    HttpUrl,
    BeforeValidator,
)
from pydantic_core import MultiHostUrl
from typing import Annotated, Any, Literal

'''
filename: config.py
This file serves as the global config file for the API Project. 
It stores application constants and loads .env
'''


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, validate_default=False
    )

    # following the full-stack fast-api template
    APP_NAME: str
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = []

    MARIADB_SERVER: str
    MARIADB_PORT: int = 3306  # default is 3306
    MARIADB_USER: str
    MARIADB_PASSWORD: str
    MARIADB_DB: str

    FIRST_SUPERUSER: str
    FIRST_SUPERUSER_PASSWORD: str

    @computed_field  # for docs: https://docs.pydantic.dev/2.0/usage/computed_fields/
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> MariaDBDsn:
        return MultiHostUrl.build(
            scheme="mariadb+mariadbconnector",
            username=self.MARIADB_USER,
            password=self.MARIADB_PASSWORD,
            host=self.MARIADB_SERVER,
            port=self.MARIADB_PORT,
            path=self.MARIADB_DB,
        )


settings = Settings()

print(settings.model_dump())
