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