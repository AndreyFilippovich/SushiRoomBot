from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DATABASE_URL: str
    API_URL: str

    class Config:
        env_file = '.env'


settings = Settings()