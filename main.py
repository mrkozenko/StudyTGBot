import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from db_functions import user_exist
from handlers import users, admin
from keyboards import get_admin_keyboard, get_user_keyboard
from states_fsm import FillForm, AdminPanel
from translates import get_translate

bot = Bot(token="6483983221:AAF9ebTU4Y6v0rnsfzbluOU77km0rtsYB0g")
dp = Dispatcher()


# хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # отримуємо текст для відповіді користувачу
    text = get_translate("start")
    user_keyboard = get_user_keyboard()
    await message.answer(text, reply_markup=user_keyboard)


# хендлер на команду /admin
@dp.message(Command("admin"))
async def admin_command(message: types.Message):
    # отримуємо текст для відповіді користувачу
    text = get_translate("admin")
    admin_keyboard = get_admin_keyboard()
    await bot.send_message(message.from_user.id, text, reply_markup=admin_keyboard)


# хендлер на текст
@dp.message(F.text == "Заповнити анкету")
async def all_text_message(message: types.Message, state: FSMContext):
    is_user_exist = user_exist(message.from_user.id)
    if is_user_exist:
        await message.answer("Ви вже заповнили анкету!")
    else:
        await state.set_state(FillForm.input_name)
        await message.answer("Введіть ваше ім'я")


@dp.message(F.text == "Пошук юзерів за містом")
async def admin_message(message: types.Message, state: FSMContext):
    await message.answer("Введіть назву міста:")
    await state.set_state(AdminPanel.search_users_by_city)


@dp.message(F.text == "Пошук юзера по айді")
async def admin_user_search(message: types.Message, state: FSMContext):
    await message.answer("Введіть айді користувача:")
    await state.set_state(AdminPanel.search_user_by_id)


async def main():
    dp.include_router(users.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
