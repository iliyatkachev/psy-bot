from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, Message

from app.SQL.sql import delete_all_channels
from app.click.keybort import admin_menu_button

delete_channel = Router()


class Del(StatesGroup):
    id_channel = State()
    full_delete = State()


@delete_channel.callback_query(F.data == 'a_c_delete')
async def delete_channels(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Del.id_channel)
    await callback.answer('Which channel do you want to delete?')
    await callback.message.delete()
    await callback.message.answer(text='Enter channel id channel')


@delete_channel.message(Del.id_channel)
async def id_del(message: Message, state: FSMContext):
    await state.update_data(id_channel=message.text)
    await state.set_state(Del.full_delete)
    await message.answer(text='The data has been collected and the channel will be deleted. To delete write YES')


@delete_channel.message(Del.full_delete)
async def full_delete(message: Message, state: FSMContext):
    if F.text.lower() == "Yas":
        data = await state.get_data()
        id_channel = data.get('id_channel', '')
        await delete_all_channels(id_channel=id_channel)
        reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
        await message.answer(text="Channel deleted!", reply_markup=reply_markup)



