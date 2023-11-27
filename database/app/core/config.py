from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "SushiRoomBot"
    POSTGRES_HOST: str = "127.0.0.1"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "SushiRoomDB"
    POSTGRES_USER: str = "SushiRoom"
    POSTGRES_PASSWORD: str = "SushiRoom"
    DATABASE_URL: str = "postgresql+asyncpg://SushiRoom:SushiRoom@127.0.0.1:5432/SushiRoomDB"
    API_URL: str = "http://127.0.0.1:8000"
    SECRET: str = 'secret'
    admin_username: str = 'admin'
    admin_password: str = 'admin'
    TOKEN: str = "6550782073:AAEb17EPeqmDw-LAEo_ItuIoOTr8qPjjUFg"

    class Config:
        env_file = '.env'


settings = Settings()