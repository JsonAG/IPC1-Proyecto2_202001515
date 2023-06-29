from fastapi import APIRouter, Response, status, HTTPException
from config.db import conn
from schemas.movie import movieEntity, moviesEntity
from models.movie import movies
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

Movie = APIRouter()


@Movie.get('/movies', response_model=list[movies], tags=["movies"])
def find_all_movies():
    return moviesEntity(conn.local.Movie.find())


@Movie.post('/movies', response_model=movies, tags=["movies"])
def create_movie(Movie: movies):
    new_movie = dict(Movie)
    del new_movie["idM"]
    id = conn.local.Movie.insert_one(new_movie).inserted_id

    Movie = conn.local.Movie.find_one({"_id": id})
    return movieEntity(Movie)


@Movie.get('/movies/{id}', response_model=movies, tags=["movies"])
def find_movie(id: str):
    return movieEntity(conn.local.Movie.find_one({"_id": ObjectId(id)}))


@Movie.put('/movies/{id}', response_model=movies, tags=["movies"])
def update_movie(id: str, Movie: movies):
    conn.local.Movie.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(Movie)})
    return movieEntity(conn.local.Movie.find_one({"_id": ObjectId(id)}))


@Movie.delete('/movies/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["movies"])
def delete_movie(id: str):
    movieEntity(conn.local.Movie.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
