from aiogram.filters.command import Command
from aiogram.types import Message

async def start_command_handler(msg: Message):
    await msg.answer('Админ вернулся!')


async def mycar_command_handler(msg: Message):
    await msg.answer('Раздел "Мои машины"')


async def tasks_command_handler(msg: Message):
    await msg.answer('Раздел "Мои задачи"')


async def profile_command_handler(msg: Message):
    await msg.answer('Личный раздел')


async def admin_command_handler(msg: Message):
    await msg.answer('Раздел администрирования')

    
def register_command_handler(dp):
    dp.message.register(start_command_handler, Command("start"))
