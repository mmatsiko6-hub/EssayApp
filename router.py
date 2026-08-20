from fastapi import APIRouter, Depends
from database import get_db
from schemas import EssayCreate, EssayUpdate
from service import EssayService
from sqlalchamy import Session

service = EsssayService()
router = APIRouter()

@router.post("/essays")
def create_essay(essay: EssayCreate, db: Session = Depends(get_db)):
   return service.create_essay(essay, db)
   

@router.get("/essays/{essay_id}")
def get_essay(essay_id: int, db: Session = Depends(get_db)):
    return service.get_essay_by_id(essay_id, db)

@router.put("/essays/{essay_id}")
def update_essay(essay_id: int, essay: EssayUpdate, db: Session = Depends(get_db)):
    return service.update_essay(essay_id, essay, db)

@router.delete("/essays/{essay_id}")
def delete_essay(essay_id: int, db: Session = Depends(get_db)):
    return service.delete_essay(essay_id, db)
