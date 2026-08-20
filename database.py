import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

def get_database_url():
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    dbname = os.getenv("POSTGRES_DB")
    return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
    
def connect_data_base():
    engine = create_engine(get_database_url())
    SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
    return engine, SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

