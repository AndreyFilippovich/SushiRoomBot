import logging
import aiohttp
from aiohttp import FormData

from app.core.config import settings


BOT_TOKEN = settings.TOKEN
BOT_SEND_PHOTO_LINK = 'https://api.telegram.org/bot{}/sendPhoto?chat_id={}'
BOT_SEND_DOCUMENT_LINK = 'https://api.telegram.org/bot{}/sendDocument?chat_id={}'
BOT_SEND_MESSAGE_LINK = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}'

logger = logging.getLogger("uvicorn")


async def send_message(
    chat_id, message=None, link=None, picture=None, file=None
):
    """
    Функция отправки одного сообщения.
    Может содержать текст, картинку, файл, ссылку.
    Можно будет использовать для рассылки индивидулальных сообщений.
    """
    async with aiohttp.ClientSession() as session:
        formdata = FormData()
        formdata.add_field('caption', message)
        formdata.add_field('parse_mode', 'HTML')
        if link:
            message += f'\n{link}'
        if picture:
            if type(picture) is str:
                response = await session.post(
                    BOT_SEND_PHOTO_LINK.format(BOT_TOKEN, chat_id),
                    data={
                        'caption': message,
                        'photo': picture,
                        'parse_mode': 'HTML',
                    },
                )
            else:
                photo = open(picture['url'], 'rb')
                formdata = FormData()
                formdata.add_field(
                    'photo',
                    photo,
                    filename=picture['filename'],
                    content_type=picture['content_type'],
                )
                formdata.add_field('caption', message)
                formdata.add_field('parse_mode', 'HTML')
                response = await session.post(
                    BOT_SEND_PHOTO_LINK.format(BOT_TOKEN, chat_id),
                    data=formdata,
                )
            message = '' if file else message
        if file:
            if type(file) is str:
                response = await session.post(
                    BOT_SEND_DOCUMENT_LINK.format(BOT_TOKEN, chat_id),
                    data={
                        'caption': message,
                        'document': file,
                        'parse_mode': 'HTML',
                    },
                )
            else:
                document = open(file['url'], 'rb')
                formdata = FormData()
                formdata.add_field('caption', message)
                formdata.add_field('parse_mode', 'HTML')
                formdata.add_field(
                    'document',
                    document,
                    filename=file['filename'],
                    content_type=file['content_type'],
                )
                response = await session.post(
                    BOT_SEND_DOCUMENT_LINK.format(BOT_TOKEN, chat_id),
                    data=formdata
                )
        if not picture and not file:
            response = await session.post(
                BOT_SEND_MESSAGE_LINK.format(BOT_TOKEN, chat_id),
                data={
                    'text': message,
                    'parse_mode': 'HTML',
                },
            )
    return response


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


async def mass_send(
    chat_ids: list, message, link=None, picture=None, file=None,
):
    """Функция массовой рассылки сообщений, по списку id."""
    file_id_flag = True
    async for chat_id in AsyncIterator(chat_ids):
        try:
            response = await send_message(
                chat_id, message, link, picture, file,
            )
            if response.status == 200 and file_id_flag:
                response_json = await response.json()
                if picture and 'photo' in response_json['result']:
                    picture = response_json['result']['photo'][0]['file_id']
                if file and 'document' in response_json['result']:
                    file = response_json['result']['document']['file_id']
                file_id_flag = False
            if response.status == 200:
                logger.info(
                    f'Сообщение {message[:30]} для {chat_id} отправлено'
                )
            else:
                info = await response.text()
                logger.warn(
                    f'Сообщение {message[:30]} для {chat_id} '
                    f'НЕ отправлено - {info}'
                )
        except Exception as exc:
            logger.error(
                f'Ошибка при отправке {message[:30]} для {chat_id} - {exc}'
            )