from os import getenv
from dotenv import load_dotenv, find_dotenv
from aiogram import types, F, Router
from aiogram.filters.command import Command
# from langchain.chat_models.gigachat import GigaChat
# from langchain.schema import HumanMessage, SystemMessage
import openai


load_dotenv(find_dotenv())
# GIGACHAT_CREDENTIALS = getenv("GIGACHAT_CREDENTIALS")
# GIGACHAT_SCOPE = getenv("GIGACHAT_SCOPE")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Добро пожаловать в наш чат с интегрированным GigaChat! Задавайте свои вопросы!')


@router.message(F.text)
async def get_answer(message: types.Message):
    from main import context_list

    # chat = GigaChat(credentials=GIGACHAT_CREDENTIALS, scope=GIGACHAT_SCOPE)
    #
    # messages = [
    #     SystemMessage(
    #         content=f"Вы - компания, обладающая списком выполненных кейсов - {context_list} с соответствующими "
    #                 f"ссылками. Используйте этот список для ответов, выбирая только подходящие кейсы (не более "
    #                 f"3-4 в ответе) и обязательно включая ссылки на них"
    #     ),
    #     HumanMessage(content=message.text)
    # ]
    # res = chat(messages)
    #
    # await message.answer(res.content)

    messages = [
        {
            "role": "system",
            "content": f"Вы - компания, обладающая списком выполненных кейсов - {context_list} с соответствующими "
                       f"ссылками. Используйте этот список для ответов, выбирая только подходящие кейсы (не более "
                       f"3-4 в ответе) и обязательно включая ссылки на них"
        },
        {
            "role": "user",
            "content": message.text
        }
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    await message.answer(chat_response)
