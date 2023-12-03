from aiogram.fsm.state import StatesGroup, State


class FillForm(StatesGroup):
    # клас станів для заповнення анкети
    input_name = State()
    input_age = State()
    input_city = State()


class AdminPanel(StatesGroup):
    # клас станів функцій адмін панелі
    search_users_by_city = State()
    search_user_by_id = State()
