import repository


def create_essay(essay):
    repository.create_essay(essay)
    return {"message": "Essay created successfully"}

def get_essay_by_id(essay_id):
    essay = repository.get_essay_by_id(essay_id)
    
    if essay is None:
        return {"message": "Essay not found"}
    return essay

def update_essay(essay_id, essay):
    rows_updated = repository.update_essay(essay_id, essay)
    
    if rows_updated == 0:
        return {"message": "Essay not found"}
    
    return {
        "message": "Essay updated successfully"
     }

def delete_essay(essay_id):
    rows_deleted = repository.delete_essay(essay_id)
    
    if rows_deleted == 0:
        return {
            "message": "Essay not found"
        }
    
    return {"message": "Essay deleted successfully"}

    