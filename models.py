from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Essay(Base):
  __tablename__ = "Essays"
  essay_id = Column(integer, primary_key = True )
  essay_title = Column(string(100), nullable = False)
  essay_author = Column(string(50), default = "ANONYMUS")
  body = Column(text, nullable = False)
  created_at = Column(TIMESTAMP(timezone = True))
  status = Column(string(10), default = "draft", nullable = False)
