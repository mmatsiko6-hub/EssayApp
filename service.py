import repository

def create_essay(essay):
    return repository.create_essay(essay)

def get_essay_by_id(essay_id):
    return repository.get_essay_by_id(essay_id)

def update_essay(essay_id, essay):
    return repository.update_essay(essay_id, essay)