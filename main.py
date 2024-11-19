import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Токен Telegram-бота
API_TOKEN = "7694610842:AAHMq8is2mPg_Fh8JGulR_ndOAWPh21LyIA"

# Ініціалізація бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хендлер для команди /start
async def start_command(message: Message):
    # Створення клавіатури
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Відкрити веб-сторінку",
                    web_app=WebAppInfo(url="https://nnpubg.github.io/futruberbot/")  # Замінити на ваш URL
                )
            ]
        ]
    )
    await message.answer("Привіт! Натисни кнопку, щоб відкрити веб-сторінку:", reply_markup=keyboard)

# Хендлер для отримання даних із WebApp
async def handle_web_app_data(message: Message):
    web_data = message.web_app_data.data
    await message.answer(f"Отримано дані з WebApp: {web_data}")

# Основна функція
async def main():
    # Реєстрація хендлерів
    dp.message.register(start_command, F.text == "/start")
    dp.message.register(handle_web_app_data, F.web_app_data)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())