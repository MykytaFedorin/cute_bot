import time
from telethon import TelegramClient
from dotenv import load_dotenv
import os
from datetime import datetime
import chatgpt
from loguru import logger

logger.remove()  # Удаляем стандартный логгер
logger.add("logs.log", level="INFO")  # Логируем инфо и ошибки
load_dotenv()
# Введи свои API ID и Hash
api_id = str(os.getenv("API_ID"))  # Замени на твой API ID
api_hash = str(os.getenv("API_HASH"))  # Замени на твой API Hash
phone_number = str(os.getenv('PHONE_NUMBER'))  # Твой номер телефона
cat_id = str(os.getenv('CAT_ID'))  # ID чата или username

# Подключаемся к Telegram
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Подключаемся к аккаунту
    await client.start(phone=phone_number)

    # Найдем чат с твоей девушкой
    chat = await client.get_entity(cat_id)  # username или ID чата

    # Бесконечный цикл для отправки сообщений
    while True:
        current_hour = datetime.now().hour
        
        # Проверяем, если текущее время в пределах 9:00 и 21:00
        if 9 <= current_hour <= 21:
            message = await chatgpt.get_answer("Придумай милое напоминание, которое можно написать моей девушке")
            await client.send_message(chat, message)  # Отправляем сообщение
        else:
            logger.info("Не дневное время. Бот спит...")

        time.sleep(3600)  # Ждем 1 час

# Запускаем клиента
with client:
    client.loop.run_until_complete(main())

