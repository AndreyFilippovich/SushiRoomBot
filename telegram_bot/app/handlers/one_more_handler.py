from aiogram.filters.command import Command
from aiogram import types, F
from app.bot import dp

from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.constants.messages import *

from app.constants import callback_data
@dp.message(Command(callback_data.SALES))
async def sales_func(message: types.Message):
    await message.answer(SALE_BUTTON,
                         parse_mode="HTML"
                         )
    

@dp.message(Command(callback_data.DELIVERY))
async def delivery_func(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить доставку",
        url="https://sushiroom24.ru/")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы оформить доставку",
        reply_markup=builder.as_markup()
    )


@dp.message(Command(callback_data.BONUSES))
async def bonuses_func(message: types.Message):
    await message.answer(
        "Какой-то текст про бонусы",
    )

@dp.message(Command(callback_data.RESTAURANTS))
async def restaurants_func(message: types.Message):
    await message.answer(
        "Наши рестораны:\n\n"
        "<b>ТРЦ Планета</b> (ул. 9 мая 77)\n"
        "<b>ТД Red SAIL</b> (ул. Алексеева д.54А)\n"
        "<b>Sushiroom</b> (ул. Капитанская 10 м-н Пятерочка 2эт.)\n",
        parse_mode="HTML"
    )


@dp.message(Command(callback_data.CONTACTS))
async def contacts_func(message: types.Message):
    await message.answer(
        "<b>SushiRoom</b>\n\n"
        "<b>Телефон</b>: +79130301155\n"
        "<b>Сайт</b>: https://sushiroom24.ru/\n"
        "<b>Инст</b>: https://instagram.com/sushiroom24\n"
        "<b>Вк</b>: https://vk.com/sushiroom24krsk\n"
        "<b>Время работы</b>: с 10:00 до 21:00\n",
        parse_mode="HTML"
    )


@dp.message(Command(callback_data.QUESTIONS))
async def questions_func(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="В диалог со службой поддержки",
        url="https://t.me/filippovich_andreyi")
    )
    await message.answer(
        "Если возникнут вопросы, то всегда можете обращаться в службу поддержки",
        reply_markup=builder.as_markup()
    )
