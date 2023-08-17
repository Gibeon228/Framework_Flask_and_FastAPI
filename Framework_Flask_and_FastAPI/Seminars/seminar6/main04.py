# Разработать API для управления списком задач. Для этого создайте модель Task со следующими полями:
#   id: int (первичный ключ)
#   title: str (название задачи)
#   description: str (описание задачи)
#   done: bool (статус выполнения задачи)
# API должно поддерживать следующие операции:
#   Получение списка всех задач: GET /tasks/
#   Получение информации о конкретной задаче: GET /tasks/{task_id}/
#   Создание новогй задачи: POST /tasks/
#   Обновление информации о пользователе: PUT /tasks/{task_id}/
#   Удаление пользователя: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///my_database.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("done", sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(max_length=32)
    description: str = Field(max_length=128)
    done: bool


class Task(BaseModel):
    id: int
    title: str = Field(max_length=32)
    description: str = Field(max_length=128)
    done: bool


@app.get("/fake_tasks/{count}")
async def create_note(count: int):
    for i in range(count):
        query = tasks.insert().values(title=f'task{i}', description=f'description{i}', done=True)
        await database.execute(query)
    return {'message': f'{count} fake tasks create'}


@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(title=task.title, description=task.description, done=task.done)
    query = tasks.insert().values(**task.dict())
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
