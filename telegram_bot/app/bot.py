import logging
from aiogram import Bot, Dispatcher

from core.config import settings
from utils.commands_menu import set_bot_commands

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.token)
dp = Dispatcher()


async def on_startup(dp):
    await set_bot_commands(dp)


async def run_polling():
    await dp.start_polling(bot)
