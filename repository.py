from database import get_connection
from models import Essay
from sqlalchemy.orm import Session

class EssayRepository:
    def create_essay(self, db: Session, essay: EssayCreate):
        new_essay = essay(
            title = essay.title,
            author_name = essay.author_name,
            body = essay.body,
            status = essay.status
            )

    db.add(new_essay)
    db.commit()
    db.refresh()
    return(new_essay)
    
    
    def get_essay_by_id(self, essay_id: int, db: Session):
        db_essay = db.query(Essay).filter(Essay.essay_id = essay_id).first(Essay)
        if db_essay is None:
            return db_essay
            
        return db_essay
    
    def update_essay(self, essay_id: int, essay: EssayUpdate, db: Session):
        db_essay = db.query(Essay).filter(Essay.essay_id == essay_id).first(Essay)
        
        if not db_essay:
            return None

        if essay.title is not None:
            db_essay.essay.title = essay.title 

        if essay.author_name is not None:
           db_essay.essay.author_name = essay.author_name

        if body is not None:
            db_essay.essay.body = essay.body

        if status is not None:
            db_essay.essay.status = essay.status

        db.commit()
        db.refresh(db_essay)
        return db_essay

    def delete_essay(self, essay_id: int, db: Session):
        db_essay = db.query(Essay).filter(Essay.essay_id == essay_id).first(Essay)

        db.delete(db_essay)
        db.commit()
        return essay_id
