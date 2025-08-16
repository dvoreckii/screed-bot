import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для расчёта стяжки пола. Напиши параметры, и я помогу рассчитать.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
