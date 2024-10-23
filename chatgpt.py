from openai import OpenAI
from dotenv import load_dotenv
from loguru import logger

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logger.remove()  # Удаляем стандартный логгер
logger.add("logs.log", level="INFO")  # Логируем инфо и ошибки

client = OpenAI()

async def get_answer(prompt: str) -> str: 
    try:
        # Логируем отправку запроса
        logger.info("Отправка запроса в OpenAI с подготовленным prompt")
        
        # Генерация сопроводительного письма через GPT
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Логируем успешное получение ответа
        logger.info("Милое письмо успешно сгенерировано")

        return str(completion.choices[0].message.content)

    except Exception as e:
        # Логируем ошибки
        logger.error(f"Ошибка при генерации письма: {e}")
        return "Произошла ошибка при генерации сопроводительного письма"

