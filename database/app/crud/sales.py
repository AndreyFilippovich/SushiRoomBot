from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sales import Sale


async def get_sale(
        session: AsyncSession,
    ) -> Sale:
    db_objs = await session.scalars(select(Sale))
    return db_objs.all()
