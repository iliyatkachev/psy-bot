from aiogram import Router, types, F
from app.click.keybort import admin_button, a_opportunities_button, button

command_r = Router()


@command_r.callback_query(F.data == 'back_a_m')
async def back(callback: types.CallbackQuery):
    await callback.answer(text='You are back in the admin menu')
    await callback.message.delete()
    user = callback.from_user.first_name
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=admin_button)
    await callback.message.answer(text=f'Hi {user}, the admin menu is available to you', reply_markup=reply_markup)


@command_r.callback_query(F.data == 'admin_opportunities')
async def back(callback: types.CallbackQuery):
    await callback.answer(text='You are in admin opportunities')
    await callback.message.delete()
    user = callback.from_user.full_name
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=a_opportunities_button)
    await callback.message.answer(text=f'Hi {user}, Here you can add or remove your administrator',
                                  reply_markup=reply_markup)


@command_r.callback_query(F.data == 'button_users')
async def back_user(callback: types.CallbackQuery):
    await callback.answer(text='Вы перешли в пользовательское меню')
    await callback.message.delete()
    user = callback.from_user.full_name
    reply_markup = types.InlineKeyboardMarkup(inline_keyboard=button)
    await callback.message.answer(text=f'Привет {user}, ты перешел в пользовательское меню!', reply_markup=reply_markup)