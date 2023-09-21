from aiogram.filters.command import Command
from aiogram import types, F
from app.bot import dp

from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.message(Command("sales"))
async def sales_func(message: types.Message):
    await message.answer("<b>Регулярные акции</b>\n"
                         "15% в день рождения (действует на сайте и на кассах)\n"
                         "10% на самовывоз (действует только на сайте)\n\n"
                         "<b>Акции в точках</b>:\n\n"
                         "<b>Ред сейл</b>:\n"
                         "-20% на горячее с 12:00 до 16:00 (бессрочная)\n"
                         "-25% на витрину с 20:00\n\n"
                         "<b>Капитанская 10</b>:\n"
                         "морс 1+1 за 129₽ (1-31/05)\n"
                         "-25% на витрину с 20:00\n\n"
                         "<b>Планета</b>:\n"
                         "-25% на витрину с 21:00",
                         parse_mode="HTML"
                         )
    

@dp.message(Command("delivery"))
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


@dp.message(Command("bonuses"))
async def bonuses_func(message: types.Message):
    await message.answer(
        "Какой-то текст про бонусы",
    )

@dp.message(Command("restaurants"))
async def restaurants_func(message: types.Message):
    await message.answer(
        "Наши рестораны:\n\n"
        "<b>ТРЦ Планета</b> (ул. 9 мая 77)\n"
        "<b>ТД Red SAIL</b> (ул. Алексеева д.54А)\n"
        "<b>Sushiroom</b> (ул. Капитанская 10 м-н Пятерочка 2эт.)\n",
        parse_mode="HTML"
    )


@dp.message(Command("contacts"))
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


@dp.message(Command("questions"))
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
