from aiogram.filters.command import Command
from aiogram import types, F
from app.bot import dp

from .callback_data import *

@dp.callback_query(F.data == "accept")
async def accept_main_menu(callback: types.CallbackQuery):
    buttons = [
        [
            types.KeyboardButton(text="Меню", callback_data="menu"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    await callback.message.answer('Теперь у вас есть меню через которое вы сможете посмотреть то-то то-то', reply_markup=keyboard)


@dp.message(F.text == "Меню")
async def main_menu(message: types.Message):
    buttons = [
            [
                types.InlineKeyboardButton(text="Акции", callback_data=SALES),
            ],
            [
                types.InlineKeyboardButton(text="Заказать доставку", callback_data=DELIVERY),
            ],
            [
                types.InlineKeyboardButton(text="Ваши бонусы", callback_data=BONUSES),
            ],
            [
                types.InlineKeyboardButton(text="Наши рестораны", callback_data=RESTAURANTS),
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data=CONTACTS),
            ],
            [
                types.InlineKeyboardButton(text="Задай вопрос", callback_data=QUESTIONS),
            ],
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(f"Главное меню", reply_markup=keyboard)