from aiogram.fsm.state import StatesGroup, State


class registration(StatesGroup):
    phone = State()
    name = State()
    date = State()
    menu = State()
