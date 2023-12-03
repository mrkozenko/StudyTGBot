from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from db_functions import create_new_user
from states_fsm import FillForm
from translates import get_translate

# фіча 3-ї версії, допомагає розділяти функціонал бота без порушення його роботи
router = Router()


# зчитування імені від юзера
@router.message(FillForm.input_name)
async def read_user_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)
    await message.answer(
        text=get_translate("answer_save")
    )
    await message.answer(
        text=get_translate("input_age")
    )
    await state.set_state(FillForm.input_age)


# зчитування імені від юзера
@router.message(FillForm.input_age)
async def read_user_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 0 or age > 100:
            await message.answer("Будь-ласка, введіть коректний вік, відповідно до умови питання.")
            return 0
        await state.update_data(age=age)

        await message.answer(
            text=get_translate("answer_save")
        )
        await message.answer(
            text=get_translate("input_city")
        )
        await state.set_state(FillForm.input_city)
    except Exception as e:
        await message.answer(f"Ваша відповідь містить помилку у питанні про вік: {message.text}")


# зчитування міста юзера
@router.message(FillForm.input_city)
async def read_city_location(message: Message, state: FSMContext):
    await message.answer(
        text=get_translate("answer_save")
    )
    await state.update_data(location=message.text)
    user_data = await state.get_data()
    report_text = await generate_user_data_report(user_data)
    #занесення даних про користувача в БД
    create_new_user(message.from_user.id,user_data["name"],message.from_user.username, user_data["age"],user_data["location"])
    await message.answer(report_text,reply_markup=None)

    await state.clear()


async def generate_user_data_report(user_data):
    #метод для форматування повідомлення з інформацією анкети
    text = f'Ваша анкета: {user_data["name"]}\nВаш вік: {user_data["age"]}\nВаше місто: {user_data["location"]}'
    return text
