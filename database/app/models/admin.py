from uuid import UUID

import bcrypt
from tortoise import fields
from tortoise.models import Model

from fastadmin import TortoiseModelAdmin, register

from models.telegram_user import TelegramUser

from app.core.db import Base

''' В authenticate я поменял username на name.
Возможно ошибка выскочит'''

@register(TelegramUser)
class UserAdmin(TortoiseModelAdmin):
    exclude = ("hash_password",)
    list_display = ("id", "username", "is_superuser", "is_active")
    list_display_links = ("id", "username")
    list_filter = ("id", "username", "is_superuser", "is_active")
    search_fields = ("username",)



    async def authenticate(self, name: str, password: str) -> UUID | int | None:
        user = await TelegramUser.filter(username=name, is_superuser=True).first()
        if not user:
            return None
        if not bcrypt.checkpw(password.encode(), user.hash_password.encode()):
            return None
        return user.id