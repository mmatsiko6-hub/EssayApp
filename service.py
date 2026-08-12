from repository import EssayRepository


class EsssayService:
    def __init__(self):
        self.repository = EssayRepository()

    def create_essay(self, essay):
        self.repository.create_essay(essay)
        return {"message": "Essay created successfully"}

    def get_essay_by_id(self, essay_id):
        essay = self.repository.get_essay_by_id(essay_id)
        
        if essay is None:
            return {"message": "Essay not found"}
        return essay

    def update_essay(self, essay_id, essay):
        rows_updated = self.repository.update_essay(essay_id, essay)
        
        if rows_updated == 0:
            return {"message": "Essay not found"}
        
        return {"message": "Essay updated successfully"}

    def delete_essay(self, essay_id):
        rows_deleted = self.repository.delete_essay(essay_id)
        
        if rows_deleted == 0:
            return {"message": "Essay not found"}
        
        return {"message": "Essay deleted successfully"}

    