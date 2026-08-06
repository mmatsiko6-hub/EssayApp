from fastapi import FastAPI
from schemas import EssayCreate, EssayUpdate
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

@app.put("/essays/{essay_id}")
def update_essay(essay_id: int, essay: EssayUpdate):
    rows_updated = service.update_essay(essay_id, essay)

    if rows_updated == 0:
        return {
            "message": "Essay not found"
        }

    return {
        "message": "Essay updated successfully"
    }