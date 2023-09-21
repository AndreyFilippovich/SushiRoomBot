import logging
from aiogram import Bot, Dispatcher

from core.config import settings
#from utils.commands_menu import set_commands

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.token)
dp = Dispatcher()


#async def on_startup(bot: Bot):
#    await set_commands(bot)


async def run_polling():
#    dp.startup.register(on_startup)
    await dp.start_polling(bot)
