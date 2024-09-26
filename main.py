from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или укажите конкретные домены, напр., ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, OPTIONS и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

class Data(BaseModel):
    data: str

@app.post("/api/data")
async def receive_data(data: Data):
    with open('data.txt', 'a') as file:
        file.write(f'{data.data}\n')
    return {"message": "Данные получены"}

@app.get("/api/data/get")
async def send_data():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
        print('Данные успешно отправлены на фронтенд')
        return JSONResponse(content={"data": content})
    except FileNotFoundError:
        print('Файл не найден')
        return JSONResponse(content={"data": ""})