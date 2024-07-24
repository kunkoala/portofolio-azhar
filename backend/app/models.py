
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, func

Base = declarative_base()

class Guestbook(Base):
    __tablename__ = "guestbook"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    created_by = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(),  nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
