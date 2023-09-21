from core.aio_client import HttpClient
from core.config import settings


async def post_user(data):
    """Функция создает нового пользователя в БД."""
    async with HttpClient() as client:
        await client.post(f"{settings.api_url}telegram_users/", data)