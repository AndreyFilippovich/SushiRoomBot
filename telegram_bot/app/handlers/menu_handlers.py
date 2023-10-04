from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, F

from app.bot import dp
from app.constants import messages, callback_data
from app.utils import promotion_processing


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
                types.InlineKeyboardButton(text="Акции", callback_data=callback_data.SALES),
            ],
            [
                types.InlineKeyboardButton(text="Заказать доставку", callback_data=callback_data.DELIVERY),
            ],
            [
                types.InlineKeyboardButton(text="Ваши бонусы", callback_data=callback_data.BONUSES),
            ],
            [
                types.InlineKeyboardButton(text="Наши рестораны", callback_data=callback_data.RESTAURANTS),
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data=callback_data.CONTACTS),
            ],
            [
                types.InlineKeyboardButton(text="Задай вопрос", callback_data=callback_data.QUESTIONS),
            ],
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(f"Главное меню", reply_markup=keyboard)


@dp.callback_query(F.data == callback_data.SALES)
async def sales_func(callback: types.CallbackQuery):
    promotions = await promotion_processing.get_promotions()
    await callback.message.answer(promotions, parse_mode="HTML")

    
@dp.callback_query(F.data == callback_data.DELIVERY)
async def delivery_func(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить доставку",
        url="https://sushiroom24.ru/")
    )
    await callback.message.answer(
        messages.DELIVERY_BUTTON,
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == callback_data.BONUSES)
async def bonuses_func(callback: types.CallbackQuery):
    await callback.message.answer(
        messages.BONUSES_BUTTON,
    )


@dp.callback_query(F.data == callback_data.RESTAURANTS)
async def restaurants_func(callback: types.CallbackQuery):
    await callback.message.answer(
        messages.RESTAURANTS_BUTTON,
        parse_mode="HTML"
    )


@dp.callback_query(F.data == callback_data.CONTACTS)
async def contacts_func(callback: types.CallbackQuery):
    await callback.message.answer(
        messages.CONTACTS_BUTTON,
        parse_mode="HTML"
    )


@dp.callback_query(F.data == callback_data.QUESTIONS)
async def questions_func(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="В диалог со службой поддержки",
        url="https://t.me/filippovich_andreyi")
    )
    await callback.message.answer(
        messages.QUESTIONS_BUTTON,
        reply_markup=builder.as_markup()
    )
