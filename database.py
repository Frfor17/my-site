from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db" # для подключения БД, для использования в движке

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # для фабрики сессий движок

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # ФАБРИКА сессий для производства сессий

Base = declarative_base()  # класс для моделей данных

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()