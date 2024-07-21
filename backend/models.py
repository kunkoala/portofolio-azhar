import datetime
from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, Text

class Guestbook(Base):
    __tablename__ = "guestbook"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    created_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.datetime.now())