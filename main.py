from fastapi import FastAPI
from schemas import EssayCreate, EssayUpdate
from service import EsssayService

service = EsssayService()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "App is running"}

@app.post("/essays")
def create_essay(essay: EssayCreate):
   return service.create_essay(essay)
   

@app.get("/essays/{essay_id}")
def get_essay(essay_id: int):
    return service.get_essay_by_id(essay_id)

@app.put("/essays/{essay_id}")
def update_essay(essay_id: int, essay: EssayUpdate):
    return service.update_essay(essay_id, essay)
    

@app.delete("/essays/{essay_id}")
def delete_essay(essay_id: int):
    return service.delete_essay(essay_id)