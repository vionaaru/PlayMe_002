from fastapi import FastAPI
# from PlayMe import PlayMe
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Заглушка для PlayMe
class PlayMe:
    @staticmethod
    async def async_get_answer(query: str) -> str:
        return f"Mock response for: {query}"

# Модель данных для POST-запросов
class Item(BaseModel):
    text: str

# создаем объект приложения
app = FastAPI()

# Переменная для логов
app.log = ""

# настройки для работы запросов
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# функция обработки get запроса + декоратор
@app.get("/")
def read_root():
    return {"message": "API is running"}

# асинхронная функция обработки post запроса + декоратор
@app.post("/api/get_answer_async")
async def get_answer_async(question: Item):
    answer = await PlayMe.async_get_answer(query=question.text)
    app.log += f"User: {question.text}\nPlayMe: {answer}\n"  # Логируем диалог
    return {"message": answer}

# Метод для получения логов диалога
@app.get("/api/log_LLM")
def get_log():
    return f"Диалог: {app.log}"