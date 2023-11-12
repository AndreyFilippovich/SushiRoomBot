import logging
from aiogram import Bot, Dispatcher

from core.config import settings
from app.handlers.birthday_handlers import scheduler, schedule_job

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.token)
dp = Dispatcher()


async def run_polling():
    scheduler.start()
    await schedule_job()
    await dp.start_polling(bot)
