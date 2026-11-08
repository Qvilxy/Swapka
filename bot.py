import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = "8728153751:AAGk-VWQyQQVhhtpXw3bYr_ldaVaF0SpVj0"

WEB_APP_URL = "https://qvilxy.github.io/swapka-app/" 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def cmd_start(message: types.Message):

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Открыть Swapka", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])

    await message.answer(
        "👋 Привет! Нажми на кнопку ниже, чтобы открыть приложение.",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
