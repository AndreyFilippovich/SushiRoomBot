from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin import I18nConfig
from starlette_admin.contrib.sqla import Admin
from starlette_admin.i18n import SUPPORTED_LOCALES

from app.admin.providers import MyAuthProvider
from app.admin.views import TGUserView, PromotionView
from app.core.config import settings
from app.core.db import engine
from app.models import telegram_user, promotions


async def configure_admin():
    """Функция конфигурации админки."""
    admin = Admin(
        engine,
        title=f'{settings.APP_TITLE} - Админ',
        base_url='/admin',
        auth_provider=MyAuthProvider(),
        middlewares=[
            Middleware(SessionMiddleware, secret_key=settings.SECRET),
        ],
        i18n_config=I18nConfig(
            default_locale="ru", language_switcher=SUPPORTED_LOCALES
        ),
    )
    admin.add_view(
        TGUserView(
            telegram_user.TelegramUser, icon='fa fa-paper-plane', label='Пользователи',
        )
    )
    admin.add_view(
        PromotionView(
            promotions.Promotion, icon='fa fa-tag', label='Акции',
        )
    )
    return admin
