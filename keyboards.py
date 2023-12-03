from aiogram import types


def get_admin_keyboard():
    kb = [
        [
            types.KeyboardButton(text="Пошук юзера по айді"),
            types.KeyboardButton(text="Пошук юзерів за містом")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard


def get_user_keyboard():
    kb = [
        [
            types.KeyboardButton(text="Заповнити анкету"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    return keyboard