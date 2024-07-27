from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, func
from pydantic import Field, BaseModel, EmailStr

Base = declarative_base()


class Guestbook(Base):
    __tablename__ = "guestbook"

    id = Column(Integer, primary_key=True, index=True)
    created_by = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

