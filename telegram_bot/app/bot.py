import logging
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6349288423:AAF2LZZ5DoPx60alRlKcaWbq_SKD1Q-TnyA")
dp = Dispatcher()


async def run_polling():
    await dp.start_polling(bot)
