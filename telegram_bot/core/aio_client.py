from aiohttp import ClientConnectionError, ClientSession

from core.logging import logger
from core.exceptions import ApiClientException


class HttpClient:
    """HTTP API клиент."""

    def __init__(self):
        """Инициализирует клиента."""
        self.session = ClientSession()

    async def _request(self, method, url, data=None, headers=None, acceptable_statuses=(200,)):
        """Отправляет запрос к API."""
        try:
            async with getattr(self.session, method)(url=url, json=data, headers=headers) as response:
                if response.status not in acceptable_statuses:
                    error_message = f"{method.upper()} request to {url=}, {data=} failed " f"with {response.status=}"
                    logger.error(error_message)
                    raise ApiClientException(error_message)
                return await response.json()
        except (ConnectionError, TimeoutError, ClientConnectionError) as error:
            error_message = f"{method.upper()} to {url=} request failed due to a " f"connection error: {str(error)}"
            logger.error(error_message)
            raise ApiClientException(error_message)

    async def post(self, url, data, headers=None, acceptable_statuses=(200, 201, 204)):
        """Отправляет POST-запрос."""
        return await self._request("post", url, data, headers, acceptable_statuses=acceptable_statuses)
    
    async def get(self, url, acceptable_statuses=(200,)):
        """Отправляет GET-запрос."""
        return await self._request("get", url, acceptable_statuses=acceptable_statuses)
    
    async def close(self):
        """Закрывает сессию клиента."""
        await self.session.close()

    async def __aenter__(self):
        """Вход в менеджер контекста."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Выход из менеджера контекста."""
        await self.close()