from aiogram.types import BotCommand
from app.constants.callback_data import *

BOT_COMMANDS = [
    BotCommand(command='sales', description='Акции'),
    BotCommand(command='delivery', description='Заказать доставку'),
    BotCommand(command='bonuses', description='Ваши бонусы'),
    BotCommand(command='restaurants', description='Наши рестораны'),
    BotCommand(command='contacts', description='Контакты'),
    BotCommand(command='questions', description='Задать вопросы'),
]
