from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.sales import get_sale

router = APIRouter()


@router.get(
    '/',
)
async def get_sales(
    session: AsyncSession = Depends(get_async_session),
):
    promotion = await get_sale(session)
    return promotion
