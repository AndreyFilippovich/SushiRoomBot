from fastapi import APIRouter

from app.api.endpoints import telegram_user_router, promotions_router

main_router = APIRouter()

main_router.include_router(
    telegram_user_router, prefix='/telegram_users', tags=['Telegram users']
)

main_router.include_router(
    promotions_router, prefix='/promotions', tags=['Promotions']
)
