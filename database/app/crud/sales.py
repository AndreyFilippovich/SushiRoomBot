from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sales import Sale


async def get_sale(
        session: AsyncSession,
    ) -> Sale:
    db_objs = await session.scalars(select(Sale))
    return db_objs.all()


async def get_sale_by_id(
        sale_id: int,
        session: AsyncSession,
    ):
    db_obj = await session.execute(select(Sale).where(Sale.id == sale_id))
    return db_obj.scalars().first()