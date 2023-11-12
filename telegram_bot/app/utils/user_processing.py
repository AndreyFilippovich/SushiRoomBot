import aiohttp

from core.aio_client import HttpClient
from core.config import settings


async def post_user(data):
    """Функция создает нового пользователя в БД."""
    async with HttpClient() as client:
        await client.post(f"{settings.api_url}telegram_users/", data)


async def get_users():
    """Функция получает всех пользователей из БД."""
    async with HttpClient() as client:
        users = await client.get(f"{settings.api_url}telegram_users/")
        return users


async def get_iiko_token():
    """Функция получает токен для авторизациии в iiko."""
    data = {"apiLogin": settings.iiko_api_key}
    async with HttpClient() as client:
        response = await client.post("https://api-ru.iiko.services/api/1/access_token",
                                data=data)
        token = response.get("token")
        return token


async def get_iiko_user(phone_number):
    """Функция получает данные пользователя из iiko."""
    token = await get_iiko_token()
    data = {
        "phone": phone_number,
        "type": "phone",
        "organizationId": settings.organizationId
    }
    async with HttpClient() as client:
        user_info = await client.post(
            "https://api-ru.iiko.services/api/1/loyalty/iiko/customer/info",
            data=data,
            headers = {'Authorization': f'bearer {token}'}
        )
        return user_info
    

async def create_iiko_user(name, phone_number, birth_day):
    """Функция регистрирует пользователя в iiko."""
    token = await get_iiko_token()
    birth_day = birth_day.split(".")
    data = {
        "id": "",
        "phone": phone_number,
        "cardTrack": "",
        "cardNumber": "",
        "name": name,
        "middleName": "",
        "surName": "",
        "birthday": f"{birth_day[2]}-{birth_day[1]}-{birth_day[0]} 12:00:00.000",
        "email": "",
        "sex": 0,
        "consentStatus": 0,
        "shouldReceivePromoActionsInfo": True,
        "referrerId": None,
        "userData": "",
        "organizationId": settings.organizationId
    }
    async with HttpClient() as client:
        await client.post(
            "https://api-ru.iiko.services/api/1/loyalty/iiko/customer/create_or_update",
            data=data,
            headers = {'Authorization': f'bearer {token}'}
        )
