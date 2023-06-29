from fastapi import FastAPI
from routes.user import user
from routes.movie import Movie


app = FastAPI(
    title="REST API with FastAPI"
)

app.include_router(user)
app.include_router(Movie)


