import datetime
import aiohttp
from aiohttp import FormData
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from core.config import settings
from app.utils import user_processing


scheduler = AsyncIOScheduler()
BOT_TOKEN = settings.token
BOT_SEND_MESSAGE_LINK = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}'
MESSAGE = ("Здравствуйте, {}!\n"
           "Сегодня у Вас большое событие — День рождения 🥳\n"
           "В честь такого события дарим Вам скидку 15% на всё наше меню!")


async def send_message(chat_id, user_name):
    async with aiohttp.ClientSession() as session:
        formdata = FormData()
        formdata.add_field('caption', MESSAGE)
        formdata.add_field('parse_mode', 'HTML')
        response = await session.post(
            BOT_SEND_MESSAGE_LINK.format(BOT_TOKEN, chat_id),
            data={
                'text': MESSAGE.format(user_name),
                'parse_mode': 'HTML',
            },
        )
    return response


async def check_birthday():
    users = await user_processing.get_users()
    current_day = datetime.date.today()
    for user in users:
        if user["birth_day"][5:][:-13] == str(current_day)[5:]:
            await send_message(user["tg_id"], user["name"])


async def schedule_job():
    scheduler.add_job(check_birthday, 'cron', day_of_week='mon-sun', hour=15, minute=00)