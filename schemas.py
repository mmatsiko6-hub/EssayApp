import uuid
from datetime import datetime
from enum import DocumentStatus


from pydantic import BaseModel, ConfigDict

class EssayCreate(BaseModel):
    title: uuid.UUID
    author_name:str
    body: str
    status: DocumentStatus = DocumentStatus.DRAFT

class EssayUpdate(BaseModel):
    title: str | None = None
    author_name:str | None = None
    body:str | None = None
    status:str | None = None

class EassyResponse(BaseModel):
    essay_id:int
    title:str
    author_name:str
    body:str
    status:str  
    created_at: datetime
