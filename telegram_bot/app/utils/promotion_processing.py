from core.aio_client import HttpClient
from core.config import settings


async def get_promotions():
    """Функция получает акции из БД."""
    async with HttpClient() as client:
        promotions = await client.get(f"{settings.api_url}promotions/")
        return promotions[0]["text"]