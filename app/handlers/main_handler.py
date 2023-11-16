from aiogram import Dispatcher
from app.handlers.message_handler import register_command_handler
#from app.handlers.callback_query_handler import register_callback_query_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = [register_command_handler, ]

    for handler in handlers:
        handler(dp)
