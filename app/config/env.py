from dotenv import load_dotenv
from os import environ

# Загружаем переменное окружение
load_dotenv()

# Сохраняем наши токены или пароли
BOT_TOKEN = environ.get('BOT_TOKEN')
ADMIN_ID = environ.get('ADMIN_ID')