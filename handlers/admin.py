from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from db_functions import get_users_by_location, get_user_by_id
from states_fsm import AdminPanel

router = Router()


@router.message(AdminPanel.search_users_by_city)
async def search_city_user(message: Message, state: FSMContext):
    city = message.text
    query_result = get_users_by_location(city)
    text = f"Користувачі за цим містом - {city}"
    if query_result:
        for row in query_result:
            #розкриваємо кортеж (синтаксичний сахар пітона)
            user_id, fullname, username, age, location = row
            text+=f"\n{user_id}, {fullname}, {username}, {age}, {location}"
    else:
        text+=" не знайдено"
    await message.answer(text)
    await state.clear()


@router.message(AdminPanel.search_user_by_id)
async def search_user_id(message: Message, state: FSMContext):
    user_id = int(message.text)
    query_result = get_user_by_id(user_id)
    text = f"Інформація про користувача з айді - {user_id}"

    if query_result:
        user_id, fullname, username, age, location = query_result
        text += f"\n{user_id}, {fullname}, {username}, {age}, {location}"
    else:
        text += " не знайдено"

    await message.answer(text)
    await state.clear()
