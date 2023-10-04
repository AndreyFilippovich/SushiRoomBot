from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.promotions import Promotion


async def get_promotion(
        session: AsyncSession,
    ) -> Promotion:
    db_objs = await session.scalars(select(Promotion))
    return db_objs.all()
