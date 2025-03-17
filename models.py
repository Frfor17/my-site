from database import Base
from sqlalchemy import Column, Integer, String

class Message():
    __tablename__= "messages"

    sms = Column(String)