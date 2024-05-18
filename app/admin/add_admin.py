from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup
from app.SQL.sql import add_administrator, fetch_administrator
from app.click.keybort import admin_menu_button

admin_router = Router()


class Admin(StatesGroup):
    name_admin = State()
    id_admin = State()
    full_admin = State()


@admin_router.callback_query(F.data == 'add_admin')
async def add_admin(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Admin.name_admin)
    await callback.answer(text='You have moved to the opportunities tab!')
    await callback.message.delete()
    await callback.message.answer(text='Enter your administrator name')


@admin_router.message(Admin.name_admin)
async def name_admin(message: Message, state: FSMContext):
    await state.update_data(name_admin=message.text)
    await state.set_state(Admin.id_admin)
    await message.answer(text='Great!\nNow write the ID of the new administrator')


@admin_router.message(Admin.id_admin)
async def id_admins(message: Message, state: FSMContext):
    await state.update_data(id_admin=message.text)
    await state.set_state(Admin.full_admin)
    await message.answer(text='Nice!\n Data collected, write "OK" to continue')


@admin_router.message(Admin.full_admin)
async def full_admin(message: Message, state: FSMContext):
    if F.text.lower() == "ОК":
        data = await state.get_data()
        name = data.get('name_admin', '')
        id_admin = data.get('id_admin', '')
        admin = int(id_admin)
        await add_administrator(name=name, id_admin=admin)
        reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
        await message.answer(text="Admin added successfully!", reply_markup=reply_markup)


@admin_router.callback_query(F.data == 'list_admin')
async def display_all_admins(callback: types.CallbackQuery):
    all_admins = await fetch_administrator()
    if all_admins:
        response_message = "Список администраторов:\n\n" + "\n".join(
            [f"ID: {admin['id_admin']}, Имя: {admin['name']}" for admin in all_admins])
    else:
        response_message = "Администраторы отсутствуют."

    await callback.message.delete()
    reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
    await callback.message.answer(text=response_message, reply_markup=reply_markup)