from fastapi import FastAPI
from schemas import EssayCreate
import service

app = FastAPI()

@app.get("/")
def home():
    return {"message": "App is running"}

@app.post("/essays")
def create_essay(essay: EssayCreate):
    service.create_essay(essay)
    return {"message": "Essay created successfully"}

@app.get("/essays/{essay_id}")
def get_essay_by_id(essay_id: int):
    essay = service.get_essay_by_id(essay_id)

    if essay is None:
        return {"message": "Essay not found"}
    return essay