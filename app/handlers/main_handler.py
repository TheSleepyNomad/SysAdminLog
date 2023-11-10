from aiogram import Dispatcher
#from app.handlers.message_handler import register_command_handlers
#from app.handlers.callback_query_handler import register_callback_query_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = []

    for handler in handlers:
        handler(dp)
