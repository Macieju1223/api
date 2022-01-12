from sqlalchemy import engine,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = 'sqlite:///./magazyn_roslin.db'

engine=create_engine(URL,connect_args={"check_same_thread":False})

sesja_localna = sessionmaker(bind=engine,autocommit=False,autoflush=False)
magazyn = declarative_base()

def get_db():
    db = sesja_localna()
    try:
        yield db
    finally:
        db.close() 