import asyncio
from os import getenv
from dotenv import load_dotenv, find_dotenv
import logging
from aiogram import Bot, Dispatcher
import handlers
from context_list import get_context_list


logging.basicConfig(level=logging.DEBUG, filename='bot_logs.conf', format=' %(asctime)s - %(levelname)s - %(message)s')

load_dotenv(find_dotenv())
TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")

bot = Bot(token=getenv('TG_BOT_TOKEN'))
context_list = get_context_list()


async def main():
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
