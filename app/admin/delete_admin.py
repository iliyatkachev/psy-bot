from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, Message
from app.SQL.sql import delete_administrator
from app.click.keybort import admin_menu_button

delete_admin = Router()


class Delete(StatesGroup):
    id_admin = State()
    full_delete_admin = State()


@delete_admin.callback_query(F.data == 'delete_admin')
async def delete_admins(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Delete.id_admin)
    await callback.answer('Which admin do you want to delete?')
    await callback.message.delete()
    await callback.message.answer(text='Entre id admin')


@delete_admin.message(Delete.id_admin)
async def delete_id_admin(message: Message, state: FSMContext):
    await state.update_data(id_admin=message.text)
    await state.set_state(Delete.full_delete_admin)
    await message.answer(text='The data has been collected and the admin will be deleted. To delete write YES')


@delete_admin.message(Delete.full_delete_admin)
async def full_delete_admin(message: Message, state: FSMContext):
    if F.text.lower() == "Yas":
        data = await state.get_data()
        id_admin = data.get('id_admin', '')
        admin = int(id_admin)
        await delete_administrator(id_admin=admin)
        reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
        await message.answer(text='Admin deleted!', reply_markup=reply_markup)

