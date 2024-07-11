import datetime
from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP, Text

class Guestbook(Base):
    __tablename__ = "guestbook"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    created_by = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.datetime.now())