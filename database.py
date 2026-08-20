import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    username = os.getenv("Postrage_username"),
    password = os.getenv("Postrage_PASSWORD"),
    mydb = os.getenv("Postrage_DSN")
    return f"postgresql+psycopy2://{username}:{password}@{mydb}"
    
def connect_data_base():
    engine = create_engine(get_database_url())
    SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
    return engine, SessionLocal
