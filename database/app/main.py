from fastapi_admin.app import app as admin_app
from fastapi import FastAPI

from app.api.telegram_user import router
from app.core.config import settings

app = FastAPI(title=settings.APP_TITLE)

app.mount("/admin", admin_app)
app.include_router(router)
