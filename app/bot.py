from aiogram import Bot, Dispatcher, executor
from aiogram.utils.exceptions import NetworkError
from app.config.env import BOT_TOKEN
from app.handlers.main_handler import register_all_handlers
from app.config.config import LOG_DIR
from loguru import logger



def __on_start_up(dp: Dispatcher):
    """
    Запускает функции на старте программы
    """
    # настройка логгера
    logger.add(LOG_DIR, format='{time} {level} {message}', level='DEBUG', rotation='10:00', serialize=True)
    logger.info('Запуск бота')

    # регистрируем все обработчики
    logger.info('Регистрация обработчиков')
    register_all_handlers(dp)
    

def start_app():
    try:
        bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
        dp = Dispatcher(bot)
        executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up(dp))
    except NetworkError:
        logger.error('Ошибка сети! Не удалось подключиться к серверу Telegram')