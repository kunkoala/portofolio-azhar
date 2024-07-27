from typing import Annotated
from collections.abc import Generator
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
SessionDependency = Annotated[Session, Depends(get_db)]