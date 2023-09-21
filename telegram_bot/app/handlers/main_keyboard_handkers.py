from aiogram import types, F
from app.bot import dp
from app.handlers.registration_handlers import *

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

@dp.callback_query(F.data == "continue")
async def main_menu(callback: types.CallbackQuery):
    await callback.message.answer('Теперь у вас есть меню через которое вы сможете посмотреть то-то то-то')
#    await set_commands(bot=Bot)
#
#async def func(message: types.Message):
#    await message.answer('как-то так')
#
#
#async def set_commands(bot: Bot):
#    commands = [
#    BotCommand(command='sales', description='Акции'),
#    BotCommand(command='delivery', description='Заказать доставку'),
#    BotCommand(command='bonuses', description='Ваши бонусы'),
#    BotCommand(command='restaurants', description='Наши рестораны'),
#    BotCommand(command='contacts', description='Контакты'),
#    BotCommand(command='questions', description='Задать вопросы')
#    ]
#
#    await bot.set_my_commands(commands, BotCommandScopeDefault())
