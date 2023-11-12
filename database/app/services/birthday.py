import logging
import aiohttp
from aiohttp import FormData

from app.core.config import settings


BOT_TOKEN = settings.TOKEN
BOT_SEND_MESSAGE_LINK = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}'
MESSAGE = ("Здравствуйте, {}!\n"
           "Сегодня у Вас большое событие — День рождения 🥳\n"
           "В честь такого события дарим Вам скидку 15% на всё наше меню!")


async def send_message(chat_id):
    async with aiohttp.ClientSession() as session:
        formdata = FormData()
        formdata.add_field('caption', MESSAGE)
        formdata.add_field('parse_mode', 'HTML')
        response = await session.post(
            BOT_SEND_MESSAGE_LINK.format(BOT_TOKEN, chat_id),
            data={
                'text': MESSAGE.format(chat_id),
                'parse_mode': 'HTML',
            },
        )
    return response


async def check_birthday():
    pass