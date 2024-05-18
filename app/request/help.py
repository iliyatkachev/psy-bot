import logging
from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from openai import AsyncOpenAI
from config import api_key


logging.basicConfig(level=logging.INFO)

help_router = Router()


class Get(StatesGroup):
    waiting_for_text = State()
    sending_request = State()


async def ask_gpt3(messages):
    try:
        client = AsyncOpenAI(api_key=api_key)
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.4
        )
        english_text = response.choices[0].message.content
        return english_text
    except Exception as e:
        logging.error(f"Error while asking GPT-3: {e}")
        return "Произошла ошибка при запросе к GPT-3. Попробуйте позже."


@help_router.callback_query(F.data == 'get')
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Get.waiting_for_text)
    await callback.message.delete()
    user = callback.from_user.first_name
    await callback.message.answer(f"Привет {user}! Опиши мне свою проблему и я постараюсь тебе помочь)")


@help_router.message(Get.waiting_for_text)
async def process_text(message: Message, state: FSMContext):
    user_message = message.text

    # Получение текущего контекста
    state_data = await state.get_data()
    messages = state_data.get('messages', [])

    # Добавление нового сообщения пользователя в контекст
    messages.append({'role': 'user', 'content': user_message})
    await state.update_data(messages=messages)

    await state.set_state(Get.sending_request)
    await message.answer("Формирую ответ...")

    try:
        # Формирование запроса к GPT-3 с учетом контекста
        response = await ask_gpt3(messages)

        # Добавление ответа бота в контекст
        messages.append({'role': 'system', 'content': response})
        await state.update_data(messages=messages)

        await message.answer(response)

        # Создание кнопки для продолжения диалога
        continue_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Продолжить диалог", callback_data="continue_dialog")]
            ]
        )
        await message.answer("Если у вас есть ещё вопросы, нажмите кнопку ниже:", reply_markup=continue_button)
    except Exception as e:
        logging.error(f"Error while processing text: {e}")
        await message.answer("Произошла ошибка при обработке вашего запроса. Попробуйте снова.")
    finally:
        await state.set_state(Get.waiting_for_text)


@help_router.callback_query(F.data == 'continue_dialog')
async def continue_dialog(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Get.waiting_for_text)
    await callback.message.delete()
    await callback.message.answer("Опишите вашу проблему, и я постараюсь помочь.")
