from aiogram import types, Router, F
from aiogram.types import InlineKeyboardMarkup

from app.click.keybort import admin_button, a_channels_button


admin_router = Router()


@admin_router.message(F.text == 'admin')
async def admin_start(message: types.Message):
    user = message.from_user.first_name
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=admin_button)
    await message.answer(text=f'Hi {user}, the admin menu is available to you', reply_markup=reply_markup)


@admin_router.callback_query(F.data == "channels")
async def channels(callback: types.CallbackQuery):
    await callback.answer('Вы перешли во вкладку каналы')
    await callback.message.delete()
    reply_markup = InlineKeyboardMarkup(inline_keyboard=a_channels_button)
    await callback.message.answer(text=f'В этом меню, вы можете добавить или удалить '
                                       f'канал, на который пользователь должен '
                                       f'подписаться', reply_markup=reply_markup)




