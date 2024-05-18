import logging
import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router
from app.keyboards import router_key

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp=Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(router_key)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')