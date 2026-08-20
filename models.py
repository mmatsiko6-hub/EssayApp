from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy import (
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Essay(Base):
  __tablename__ = "essays"
  
  essay_id = Column(Integer, primary_key = True, index = True )
  essay_title = Column(String(100), nullable = False)
  essay_author = Column(String(50), default = "ANONYMUS")
  body = Column(Text, nullable = False)
  created_at = Column(DATETIME(timezone = True), server_default = func.now())
  status = Column(String(10), default = "draft", nullable = False)
