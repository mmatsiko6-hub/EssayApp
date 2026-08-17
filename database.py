import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def connect_data_base():
    def Database_URL():
        username = os.getenv("Postrage_username"),
        password = os.getenv("Postrage_PASSWORD"),
        mydb = os.getenv("Postrage_DSN")
        return f"postragespl+psycopy2://{username}:{password}@{mydb}"
        
    engine = create_engine(Database_URL)

    SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

    return engine, SessionLocal

