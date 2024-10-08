from typing import Annotated, List, Any

from app.api.dependencies import SessionDependency as Session
from app.models import Guestbook, GuestbookCreate, GuestbookPublic, Guests, Message
from sqlmodel import select, func

from fastapi import APIRouter, HTTPException, Path

router = APIRouter()

tags_metadata = [
    {
        "name": "guestbook",
        "description": "Operations related to the guestbook",
    }
]


'''
TODO: Implement the following API endpoints for the guestbook:
1. Create a new entry in the guestbook
2. Read all entries in the guestbook
3. Read a specific entry in the guestbook
4. Update a specific entry in the guestbook
5. Delete a specific entry in the guestbook
'''



@router.get("/guestbook", response_model=Guests, tags=['guestbook'])
async def read_guestbook_stats(session: Session, skip: int = 0, limit: int = 100) -> Any:
    """
    Get the total number of entries in the guestbook
    """
    # Get the total count of entries
    count_statement = select(func.count()).select_from(Guestbook)
    count_result = session.exec(count_statement).one()

    # Get the guestbook entries
    guests_statement = select(Guestbook).offset(skip).limit(limit)
    guests_result = session.exec(guests_statement).all()

    if count_result == 0:
        raise HTTPException(status_code=404, detail="No guestbook entries found")

    # Convert SQLAlchemy models to Pydantic models
    guests = [GuestbookPublic.model_validate(guest) for guest in guests_result]
    
    return Guests(data=guests, count=count_result)

# get a specific entry in the guestbook
@router.get("/guestbook/{entry_id}", response_model=GuestbookPublic, tags=['guestbook'])
async def read_guestbook_entry(entry_id: Annotated[int, Path()], session: Session):
    """
    Get a specific entry in the guestbook
    """
    # much more simpler code in sqlmodel
    entry = session.get(Guestbook, entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Guestbook entry not found")
    return entry

# create a new entry in the guestbook
@router.post("/guestbook", response_model=GuestbookPublic, tags=['guestbook'])
async def create_guestbook_entry(guestbook_in: GuestbookCreate, session: Session):
    """
    Create a new guest entry in the guestbook
    """
    guest = Guestbook.model_validate(guestbook_in)
    session.add(guest)
    session.commit()
    session.refresh(guest)
    return guest

# delete a specific entry in the guestbook
@router.delete("/guestbook/{entry_id}", response_model=Message, tags=['guestbook'])
def delete_guestbook_entry(entry_id: Annotated[int, Path()], session: Session) -> Message:
    """
    Delete an item from the guestbook
    """
    guest = session.get(Guestbook, entry_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guestbook entry not found")
    # TODO: add a conditional for checking current user id with the guestbook entry id relation
    session.delete(guest)
    session.commit()
    return Message(message="Guestbook entry deleted successfully")
    
    
    
