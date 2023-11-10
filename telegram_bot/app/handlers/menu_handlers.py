from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, F

from app.bot import dp
from app.constants import messages, callback_data
from app.utils import promotion_processing
from app.states import registration
from app.utils import user_processing


@dp.callback_query(F.data == "accept")
async def accept_main_menu(callback: types.CallbackQuery, state: FSMContext):
    buttons = [
        [
            types.KeyboardButton(text="Меню", callback_data="menu"),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    await callback.message.answer(messages.MENU_MESSAGE, reply_markup=keyboard)
    await state.set_state(registration.menu)


@dp.message(registration.menu, F.text == "Меню")
async def main_menu(message: types.Message, state: FSMContext):
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


@dp.callback_query(registration.menu, F.data == callback_data.BONUSES)
async def bonuses_func(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_phone = user_data['phone']
    user_info = await user_processing.get_iiko_user(user_phone)
    await callback.message.answer(
        f"У вас {int(user_info['walletBalances'][0]['balance'])} бонусов"
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
