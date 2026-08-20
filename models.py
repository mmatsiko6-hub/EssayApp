from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy import (
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    ForeignKey,
    
)

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from enum import Status

Base = declarative_base()

class Essay(Base):
  __tablename__ = "essays"
  
  essay_id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True )
  essay_title: Mapped[str] = mapped_column(String(100), nullable = False)
  essay_author: Mapped[str] = mapped_column(String(50), default = "ANONYMUS")
  body: Mapped[str] = mapped_Column(Text, nullable = False)
  created_at: Mapped[DateTime] = Column(DATETIME(timezone = True), server_default = func.now())
    
  status: Mapped[DocumentStatus] = mapped_column(
  Enum(DocumentStatus, name="documentstatus"),
  nullable=False,
  default=DocumentStatus.DRAFT
          
  authors = relationship("Author", back_populates = "essay")

class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key = True, index = True)
    essay_id = Column(Integer, ForeignKey(essays.essay_id))
    author_name = Column(String(50))
    essays = Column(Integer)


    

    

    
