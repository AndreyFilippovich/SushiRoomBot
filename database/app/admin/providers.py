from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

from app.core.config import settings

ADMIN_USERNAME = settings.admin_username
ADMIN_PASSWORD = settings.admin_password


class MyAuthProvider(AuthProvider):
    """
    Класс провайдера аутентификации админки.
    """

    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        if len(username) < 3:
            raise FormValidationError(
                {'username': 'Ensure username has at least 03 characters'}
            )
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session.update({'username': username})
            return response
        raise LoginFailed('Invalid username or password')

    async def is_authenticated(self, request) -> bool:
        if request.session.get('username', None) == ADMIN_USERNAME:
            request.state.user = ADMIN_USERNAME
            return True
        return False

    def get_admin_user(self, request: Request) -> AdminUser:
        return AdminUser(
            username=ADMIN_USERNAME,
        )

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response