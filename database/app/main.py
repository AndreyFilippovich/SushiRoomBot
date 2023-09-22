from fastapi import FastAPI

from app.api.telegram_user import router
from app.core.config import settings

app = FastAPI(title=settings.APP_TITLE)
app.include_router(router)
