from pydantic import BaseModel

class EssayCreate(BaseModel):
    title:str
    author_name:str
    body: str
    status: str

class EssayUpdate(BaseModel):
    title: str
    author_name:str
    body:str
    status:str    

class EassyResponse(BaseModel):
    essay_id:int
    title:str
    author_name:str
    body:str
    status:str    