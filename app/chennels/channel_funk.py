from aiogram.types import Message
from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.click.keybort import admin_menu_button
from app.SQL.sql import add_channel, fetch_urls_and_ids

form_channel = Router()


class Form(StatesGroup):
    name = State()
    url = State()
    id_channel = State()
    full_channel = State()


@form_channel.callback_query(F.data == "a_c_add")
async def channels(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.name)
    await callback.answer('Вы перешли во вкладку каналы')
    await callback.message.delete()
    await callback.message.answer(text='Добавить название канала')


@form_channel.message(Form.name)
async def name_com(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.url)
    await message.answer(text='Отлично!\nТеперь напишите URL нового канала')


@form_channel.message(Form.url)
async def url_com(message: Message, state: FSMContext):
    await state.update_data(url=message.text)
    await state.set_state(Form.id_channel)
    await message.answer(text='Хорошо!\nТеперь введите ID канала')


@form_channel.message(Form.id_channel)
async def id_com(message: Message, state: FSMContext):
    await state.update_data(id_channel=message.text)
    await state.set_state(Form.full_channel)
    await message.answer(text='Готово!\nТеперь вам нужно написать ОК для продолжения добавления')


@form_channel.message(Form.full_channel)
async def full_channel(message: Message, state: FSMContext):
    if message.text.lower() == "ок":
        data = await state.get_data()
        name = data.get('name', '')
        url = data.get('url', '')
        id_channel = data.get('id_channel', '')
        await add_channel(name_channel=name, url=url, id_channel=id_channel)
        reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
        await message.answer(text="Канал успешно добавлен!", reply_markup=reply_markup)


async def channels_add(callback: types.CallbackQuery):
    public_urls = await fetch_urls_and_ids()
    if public_urls:
        keyboard_public = [
                [InlineKeyboardButton(text="Подпишись👈", url=url)]
                for url in public_urls
            ]
        keyboard_public.append([InlineKeyboardButton(text="Проверить подписку", callback_data='check_me')])
        buttons = InlineKeyboardMarkup(inline_keyboard=keyboard_public)
        await callback.message.answer('⚠️ Пожалуйста, подпишитесь на все паблики для использования бота.',
                                      reply_markup=buttons)
        await callback.message.delete()
    else:
        await callback.message.answer("Извините, у вас ещё нет пабликов")
