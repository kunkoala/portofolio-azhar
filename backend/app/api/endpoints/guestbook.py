from typing import Annotated

from app.api.dependencies import SessionDependency as Session
from app.models import Guestbook, GuestbookCreate

from fastapi import APIRouter, HTTPException, Path

router = APIRouter()

'''
TODO: Implement the following API endpoints for the guestbook:
1. Create a new entry in the guestbook
2. Read all entries in the guestbook
3. Read a specific entry in the guestbook
4. Update a specific entry in the guestbook
5. Delete a specific entry in the guestbook
'''

# get all entries in the guestbook
@router.get("/api/guestbook")
async def read_guestbook(session: Session):
    guestbook = session.query(Guestbook).all()
    return guestbook

# get a specific entry in the guestbook
@router.get("/api/guestbook/{entry_id}")
async def read_guestbook_entry(entry_id: Annotated[int, Path()], session: Session):
    return db.query(Guestbook).filter(Guestbook.id == entry_id).first()
