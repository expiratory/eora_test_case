import asyncio
from os import getenv
from dotenv import load_dotenv, find_dotenv
import logging
from aiogram import Bot, Dispatcher
from link_list import link_list
import handlers


logging.basicConfig(level=logging.DEBUG, filename='logs', format=' %(asctime)s - %(levelname)s - %(message)s')

load_dotenv(find_dotenv())
TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")

bot = Bot(token=getenv('TG_BOT_TOKEN'))

headers_list = []

with open('headers.txt', 'r') as f:
    for line in f.readlines():
        header = line
        if header != '':
            header = header.replace('\n', '')
            headers_list.append(header)

context_list = []

for header, link in zip(headers_list, link_list):
    context_list.append([header, link])


async def main():
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
