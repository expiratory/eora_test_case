from fastapi import FastAPI, Request
from giga_chat import ask_gigachat
from chat_gpt import ask_chat_gpt
from context_list import get_context_list
from models import Question, Answer
import logging
import uvicorn
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ai', choices=('chatgpt', 'gigachat'), default='chatgpt', help="Выбор языковой "
                    "модели, ChatGPT или GigaChat, по умолчанию - ChatGPT")
args = parser.parse_args()


app = FastAPI()
context_list = get_context_list()

logging.basicConfig(
    level=logging.DEBUG,
    filename='fastapi_logs.conf',
    format=' %(asctime)s - %(levelname)s - %(message)s'
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    logging.info(f"{request.method} {request.url} {response.status_code}")
    return response


@app.post('/get_answer/', response_model=Answer)
async def get_answer(question: Question):
    if args.ai == 'gigachat':
        answer = ask_gigachat(question, context_list)
    else:
        answer = ask_chat_gpt(question.question, context_list)
    return Answer(answer=answer)


if __name__ == '__main__':
    uvicorn.run(app)
