from aiogram.filters.command import Command
from aiogram.types import Message

async def start_command_handler(msg: Message):
    await msg.answer('Админ вернулся!')



def register_command_handler(dp):
    dp.message.register(start_command_handler, Command("start"))
