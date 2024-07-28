from typing import Annotated
from collections.abc import Generator
from sqlmodel import Session
from fastapi import Depends

from app.database import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
SessionDependency = Annotated[Session, Depends(get_db)]