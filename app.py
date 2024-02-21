from fastapi import FastAPI
from giga_chat import ask_gigachat
from chat_gpt import ask_chat_gpt
from context_list import get_context_list
import logging
from models import Question, Answer


# logging.basicConfig(level=logging.DEBUG, filename='logs.txt', format=' %(asctime)s - %(levelname)s - %(message)s')  #prod
logging.basicConfig(level=logging.INFO)  # dev

app = FastAPI()
context_list = get_context_list()


@app.post('/get_answer/', response_model=Answer)
async def get_answer(question: Question):
    # answer = ask_gigachat(question, context_list)
    answer = ask_chat_gpt(question.question, context_list)
    return Answer(answer=answer)
