from aiogram import Dispatcher

from app.constants.keyboards import BOT_COMMANDS


async def set_bot_commands(dp):
    '''Открывает меню команд бота'''
    await dp.bot.set_my_commands(commands=BOT_COMMANDS)
