from aiogram.filters.command import Command
from aiogram import types, F
from app.bot import dp

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.handlers.registration_handlers import *
from app.constants.messages import *

from app.constants import callback_data



@dp.callback_query(F.data == callback_data.SALES)
async def sales_func(callback: types.CallbackQuery):
    await callback.message.answer(SALE_BUTTON, parse_mode="HTML")

    
@dp.callback_query(F.data == callback_data.DELIVERY)
async def delivery_func(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Оформить доставку",
        url="https://sushiroom24.ru/")
    )
    await callback.message.answer(
        DELIVERY_BUTTON,
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == callback_data.BONUSES)
async def bonuses_func(callback: types.CallbackQuery):
    await callback.message.answer(
        BONUSES_BUTTON,
    )


@dp.callback_query(F.data == callback_data.RESTAURANTS)
async def restaurants_func(callback: types.CallbackQuery):
    await callback.message.answer(
        RESTAURANTS_BUTTON,
        parse_mode="HTML"
    )


@dp.callback_query(F.data == callback_data.CONTACTS)
async def contacts_func(callback: types.CallbackQuery):
    await callback.message.answer(
        CONTACTS_BUTTON,
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
        QUESTIONS_BUTTON,
        reply_markup=builder.as_markup()
    )
