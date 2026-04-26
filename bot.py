import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Напиши мне что-нибудь, и я отправлю это обратно.")

# Обработчик всех сообщений
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
