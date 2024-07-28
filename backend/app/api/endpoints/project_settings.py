from typing import Annotated
from functools import lru_cache

from app.api.dependencies import SessionDependency as Session
from app.models import Guestbook
from app.core.config import settings

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@lru_cache
def get_settings():
    return settings

@router.get("/project_settings/hello")
async def read_root():
    return {"message": "Hello World! This API is now working yippie!"}


@router.get("/project_settings/settings")
async def info(settings: Annotated[settings, Depends(get_settings)]): # type: ignore
    return {
        "app_name": settings.APP_NAME,
        "ENV (prod or dev)": settings.ENVIRONMENT,
        "DATABASE_ENV": str(settings.SQLALCHEMY_DATABASE_URI),
    }
