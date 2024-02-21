from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
GIGACHAT_CREDENTIALS = getenv("GIGACHAT_CREDENTIALS")
GIGACHAT_SCOPE = getenv("GIGACHAT_SCOPE")


def ask_gigachat(question, context_list):
    chat = GigaChat(credentials=GIGACHAT_CREDENTIALS, scope=GIGACHAT_SCOPE)

    messages = [
        SystemMessage(
            content=f"Вы - компания, обладающая списком выполненных кейсов - {context_list} с соответствующими "
                    f"ссылками. Используйте этот список для ответов, выбирая только подходящие кейсы (не более "
                    f"3-4 в ответе) и обязательно включая ссылки на них"
        ),
        HumanMessage(content=question)
    ]
    res = chat(messages)
    answer = res.content

    return answer
