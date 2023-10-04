from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.promotions import get_promotion

router = APIRouter()


@router.get(
    '/',
)
async def get_promotions(
    session: AsyncSession = Depends(get_async_session),
):
    promotion = await get_promotion(session)
    return promotion

