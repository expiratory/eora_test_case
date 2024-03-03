from aiogram import types, F, Router
from aiogram.filters.command import Command
from giga_chat import ask_gigachat
from chat_gpt import ask_chat_gpt
from context_list import get_context_list


router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Добро пожаловать в наш чат с интегрированным GigaChat! Задавайте свои вопросы!')


@router.message(F.text)
async def get_answer(message: types.Message):
    from main import args

    context_list = get_context_list()
    if args.ai == 'gigachat':
        answer = ask_gigachat(message.text, context_list)
    else:
        answer = ask_chat_gpt(message.text, context_list)
    await message.answer(answer)
