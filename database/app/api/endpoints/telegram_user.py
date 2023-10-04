from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.telegram_user import create_telegram_user
from app.schemas.telegram_user import TelegramUserCreate

router = APIRouter()


@router.post(
    '/',
    response_model=TelegramUserCreate,
)
async def create_new_telegram_user(
    telegram_user: TelegramUserCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_telegram_user = await create_telegram_user(telegram_user, session)
    return new_telegram_user
