from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.telegram_user import TelegramUser
from app.schemas.telegram_user import TelegramUserCreate


async def create_telegram_user(
        new_telegram_user: TelegramUserCreate,
        session: AsyncSession,
    ) -> TelegramUser:

    new_discord_user_data = new_telegram_user.model_dump()
    db_discord_user = TelegramUser(**new_discord_user_data)
    session.add(db_discord_user)
    await session.commit()
    await session.refresh(db_discord_user)
    return db_discord_user


async def get_all_users_ids(
        session: AsyncSession,
    ):
    tg_users_ids = await session.execute(select(TelegramUser.tg_id))
    return tg_users_ids.scalars().all()