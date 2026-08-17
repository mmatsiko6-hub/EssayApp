from pydantic import BaseModel

class EssayCreate(BaseModel):
    title:str
    author_name:str
    body: str
    status: str

class EssayUpdate(BaseModel):
    title: str | None = None
    author_name:str | None = None
    body:str | None = None
    status:str | None = None

class EssayResponse(BaseModel):
    essay_id:int
    title:str
    author_name:str
    body:str
    status:str    
