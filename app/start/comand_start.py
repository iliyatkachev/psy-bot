import random
from aiogram import types, F, Router
from aiogram.filters import Command, CommandStart
from app.SQL.sql import fetch_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.admin.admin import admin_start
from app.click.keybort import button


start_router = Router()


#command start
@start_router.message(CommandStart())
async def protect(message: types.Message):
    if message.from_user.id not in await fetch_admin():
        num1 = random.randint(1, 11)
        num2 = random.randint(1, 11)
        correct_answer = num1 + num2
        buttons = [
            types.InlineKeyboardButton(text=str(random.randint(2, 21)), callback_data='num_1'),
            types.InlineKeyboardButton(text=str(random.randint(2, 21)), callback_data='num_2'),
            types.InlineKeyboardButton(text=str(random.randint(2, 21)), callback_data='num_3'),
        ]

        correct_position = random.randint(0, len(buttons))

        buttons.insert(correct_position, types.InlineKeyboardButton(text=str(correct_answer), callback_data="correct"))

        protect_buttons = [buttons]

        reply_markup = types.InlineKeyboardMarkup(inline_keyboard=protect_buttons)
        await message.answer(text=f"🛡 Для запуска, надо пройти проверку безопасности. Сколько будет {num1} + {num2}?",
                             reply_markup=reply_markup)
    else:
        return await admin_start(message)


@start_router.callback_query(F.data == "correct")
async def start(callback: types.CallbackQuery):
    await callback.message.delete()
    reply_markup = InlineKeyboardMarkup(inline_keyboard=button)
    await callback.message.answer(text=f"Привет {callback.from_user.username}!", reply_markup=reply_markup)


@start_router.message(Command("help", prefix="/!"))
async def hendel_help(message: types.Message):
    button = [
        [
            InlineKeyboardButton(text="Служба Поддержки🥸", url="https://t.me/Iltk01")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=button)
    await message.answer(text="Если у вас возникли проблемы, обратитесь в службу поддержки...",
                         reply_markup=reply_markup)


#pass