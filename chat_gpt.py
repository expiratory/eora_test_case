import openai
from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


def ask_chat_gpt(question, context_list):
    openai.api_key = getenv("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": f"Вы - компания, обладающая списком выполненных кейсов - {context_list} с соответствующими "
                       f"ссылками. Используйте этот список для ответов, выбирая только подходящие кейсы (не более "
                       f"3-4 в ответе) и обязательно включая ссылки на них"
        },
        {
            "role": "user",
            "content": question
        }
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    answer = completion.choices[0].message.content

    return answer
