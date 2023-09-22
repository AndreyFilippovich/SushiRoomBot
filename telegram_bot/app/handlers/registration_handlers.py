from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from datetime import datetime

from app.bot import dp
from app.states import registration
from app.utils import user_processing


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    button_phone = [
        [
            types.KeyboardButton(text="Поделиться номером", request_contact=True),
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=button_phone,
        resize_keyboard=True
    )
    await message.answer(f"Здравствуйте!\n"
                         f"Приветственное сообщение при регистрации.\n"
                         f"Нажмите кнопку <b>«Поделиться номером»</b>, чтобы продолжить", parse_mode="HTML", reply_markup=keyboard)
    await state.set_state(registration.phone)


@dp.message(registration.phone, F.contact)
async def handle_contact(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await message.answer(f"Напишите ваше Имя\n"
                         f"Всегда приятно, когда к вам обращаются по имени", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(registration.name)


@dp.message(registration.phone)
async def handle_contact_error(message: types.Message, state: FSMContext):
    await message.answer(f"Чтобы продолжить, нажмите кнопку «Поделиться номером»")
    await state.set_state(registration.phone)


@dp.message(registration.name, F.text)
async def handle_name(message: types.Message, state: FSMContext):
    buttons = [
            [
                types.InlineKeyboardButton(text="Подтвердить", callback_data="accept_name"),
                types.InlineKeyboardButton(text="Изменить", callback_data="again_name"),
            ],
        ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(f"Вы указали имя - {message.text}\n", reply_markup=keyboard)
    await state.set_state(registration.name)


@dp.callback_query(F.data == "again_name")
async def again_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Напишите ваше Имя")
    await state.set_state(registration.name)


@dp.callback_query(F.data == "accept_name")
async def handle_name(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(name=callback.message.text.split(' ')[-1])
    await callback.message.answer(f"Напишите вашу Дату Рождения в формате 31.01.1999\n"
                                  f"Мы будем поздравлять вас и дарить бонусы в честь вашего дня рождения")
    await state.set_state(registration.date)


@dp.message(registration.date, F.text)
async def handle_date(message: types.Message, state: FSMContext):
    try:
        datetime.strptime(message.text, '%d.%m.%Y')
        await state.update_data(date=message.text)
        user_data = await state.get_data()
        buttons = [
            [
                types.InlineKeyboardButton(text="Подтвердить", callback_data="accept"),
            ],
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        await message.answer(f"Имя - {user_data['name']}\n"
                             f"Дата Рождения - {user_data['date']}\n"
                             f"Телефон - {user_data['phone']}\n",
                             reply_markup=keyboard)
        data = {
            "name": user_data['name'],
            "tg_id": message.from_user.id,
            "phone_number": user_data['phone'],
            "birth_day": user_data['date']
        }
        await user_processing.post_user(data)
        await state.clear()
    except:
        await message.answer(f"Введена некоректная дата, повторите попытку")
