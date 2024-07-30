from fastapi import APIRouter

from app.api.endpoints import guestbook, project_settings

api_router = APIRouter()

api_router.include_router(guestbook.router, tags=["guestbook"], prefix="/guestbook")

api_router.include_router(project_settings.router, tags=["project_settings"], prefix="/project_settings")