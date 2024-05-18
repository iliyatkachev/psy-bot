import asyncio
import logging
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config import bot_token
from app.start import comand_start
from app.admin import admin, add_admin, delete_admin
from app.chennels import chennel_funk
from app.chennels import delete_channel
from app.commands import command_processing, statist
from app.mailing_fun import mailing
from app.request import help

dp = Dispatcher()
dp.include_routers(comand_start.start_router, admin.admin_router, chennel_funk.form_channel,
                   delete_channel.delete_channel, command_processing.command_r, statist.stat_router,
                   mailing.form_router, add_admin.admin_router, delete_admin.delete_admin, help.help_router)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())


