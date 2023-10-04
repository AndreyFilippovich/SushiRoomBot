from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings
from app.admin.core import configure_admin

app = FastAPI(title=settings.APP_TITLE)
app.include_router(main_router)

@app.on_event('startup')
async def startup():
    admin = await configure_admin()
    admin.mount_to(app)