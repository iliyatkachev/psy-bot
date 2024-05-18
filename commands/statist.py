from aiogram import F, types, Router
from aiogram.types import InlineKeyboardMarkup
from app.SQL.sql import s_full_users
from app.click.keybort import a_stat_button, admin_menu_button

stat_router = Router()


@stat_router.callback_query(F.data == "a_stat")
async def a_stat(callback: types.CallbackQuery):
    await callback.answer('Вы перешли во вкладку статистика')
    await callback.message.delete()
    reply_markup = InlineKeyboardMarkup(inline_keyboard=a_stat_button)
    await callback.message.answer(text='Управление пользовательским меню', reply_markup=reply_markup)


@stat_router.callback_query(F.data == 's_full_users')
async def full_users(callback: types.CallbackQuery):
    await callback.answer('Display of users')
    await callback.message.delete()
    full_user = await s_full_users()
    reply_markup = InlineKeyboardMarkup(inline_keyboard=admin_menu_button)
    await callback.message.answer(f'<b>Users:</b>{full_user}', reply_markup=reply_markup)


