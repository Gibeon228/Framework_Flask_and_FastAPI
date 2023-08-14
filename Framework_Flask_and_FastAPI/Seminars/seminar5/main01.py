# Создать API для управления списком задач. Приложение должно иметь возможность создавать,
# обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task для хранения задач.
# Создайте маршрут для получения списка задач(метод GET).
# Создайте маршрут для создания новой задачи(метод POST).
# Создайте маршрут для обновления задачи(метод PUT).
# Создайте маршрут для удаления задачи(метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


tasks = []


@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks


@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    task.id = len(tasks) + 1
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            task.id = task_id
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i in range(len(tasks)):
        if tasks[i].id == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")