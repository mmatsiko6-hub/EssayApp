from fastapi import APIRouter
from schemas import EssayCreate, EssayUpdate
from service import EsssayService

service = EsssayService()
router = APIRouter()

@router.get("/")
def home():
    return {"message": "App is running"}

@router.post("/essays")
def create_essay(essay: EssayCreate):
   return service.create_essay(essay)
   

@router.get("/essays/{essay_id}")
def get_essay(essay_id: int):
    return service.get_essay_by_id(essay_id)

@router.put("/essays/{essay_id}")
def update_essay(essay_id: int, essay: EssayUpdate):
    return service.update_essay(essay_id, essay)

@router.delete("/essays/{essay_id}")
def delete_essay(essay_id: int):
    return service.delete_essay(essay_id)