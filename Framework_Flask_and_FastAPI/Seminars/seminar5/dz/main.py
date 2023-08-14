# Создать API для получения списка фильмов по жанру. Приложение должно иметь
# возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру(метод GET).
# Создайте маршрут для создания новоого фильма(метод POST).
# Создайте маршрут для обновления информации о фильме(метод PUT).
# Создайте маршрут для удаления фильма(метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []

count = 10
for movie in range(1, count + 1):
    movies.append(Movie(id=movie,
                        title=f'Title{movie}',
                        description=f'DESCRIPTION{movie}',
                        genre=random.choice(["scary", "comedy", "thriller", "science fiction", "drama"])))


@app.get("/", response_model=List[Movie])
async def get_movies():
    return movies


@app.get("/movies/", response_model=List[Movie])
async def get_movies(movies_genre: str):
    movies_genres = []
    for i in range(len(movies)):
        if movies[i].genre == movies_genre:
            movies_genres.append(movies[i])
    return movies_genres


@app.post("/movies/", response_model=Movie)
async def create_movie(movie: Movie):
    movie.id = len(movies) + 1
    movies.append(movie)
    return movie


@app.put("/movies/{movie_id}", response_model=Movie)
async def update_movie(movie_id: int, movie: Movie):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movie.id = movie_id
            movies[i] = movie
            return movie
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            del movies[i]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
