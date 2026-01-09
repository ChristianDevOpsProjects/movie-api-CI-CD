# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/movies")
def get_movies():
    return [
        {"title": "Inception", "year": 2010},
        {"title": "Interstellar", "year": 2014},
        {"title": "The Matrix", "year": 1999}
    ]

@app.get("/health")
def health():
    return {"status": "ok"}
