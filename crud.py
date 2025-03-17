from sqlalchemy.orm import Session
from models import Message

def get_messages(db: Session):   # объект Сессион типа ДБ, передаём функцию, чтобы работала с  нашей БД
    return db.query(Message).all()  # делает запрос к бд, вытягивает все messages
