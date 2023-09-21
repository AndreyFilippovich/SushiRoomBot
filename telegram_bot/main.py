import asyncio

from app.bot import run_polling
from app.handlers.one_more_handler import (sales_func, delivery_func, bonuses_func,
                                           restaurants_func, contacts_func, 
                                           questions_func)


async def start():
    """Запуск бота."""
    await run_polling()

async def sales():
    await sales_func()

async def delivery():
    await delivery_func()

async def bonuses():
    await bonuses_func()

async def restaurants():
    await restaurants_func()

async def contacts():
    await contacts_func()

async def questions():
    await questions_func()


if __name__ == "__main__":
    asyncio.run(start())
    asyncio.run(sales())
    asyncio.run(delivery())
    asyncio.run(bonuses())
    asyncio.run(restaurants())
    asyncio.run(contacts())
    asyncio.run(questions())

