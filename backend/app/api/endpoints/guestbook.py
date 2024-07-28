from typing import Annotated, List

from app.api.dependencies import SessionDependency as Session
from app.schemas import GuestbookPublic, GuestbookCreate, Guests, Message
from app.models import Guestbook

from sqlalchemy import select, func

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

@router.get("/guestbook", response_model=Guests)
async def read_guestbook_stats(session: Session, skip: int = 0, limit: int = 100):
    """
    Get the total number of entries in the guestbook
    """
    # Get the total count of entries
    count_statement = select(func.count()).select_from(Guestbook)
    count_result = session.execute(count_statement).scalar()

    # Get the guestbook entries
    guests_statement = select(Guestbook).offset(skip).limit(limit)
    guests_result = session.execute(guests_statement).scalars().all()

    if count_result == 0:
        raise HTTPException(status_code=404, detail="No guestbook entries found")

    # Convert SQLAlchemy models to Pydantic models
    guests = [GuestbookPublic.model_validate(guest) for guest in guests_result]

    print(guests)
    return Guests(data=guests, count=count_result)

# get all entries in the guestbook
# @router.get("/guestbook", response_model=List[Guestbook])
# async def read_guestbook(session: Session):
#     """
#     Get all entries in the guestbook
#     """
#     guestbook = session.query(Guestbook).all()
#     return guestbook

# get a specific entry in the guestbook
@router.get("/guestbook/{entry_id}", response_model=GuestbookPublic)
async def read_guestbook_entry(entry_id: Annotated[int, Path()], session: Session):
    entry = session.query(Guestbook).filter(Guestbook.id == entry_id).first()
    if entry is None:
        raise HTTPException(status_code=404, detail="Guestbook entry not found")
    return entry


# create a new entry in the guestbook
@router.post("/guestbook", response_model=GuestbookPublic)
async def create_guestbook_entry(guestbook_in: GuestbookCreate, session: Session):
    """
    Create a new guest entry in the guestbook
    """
    guest = Guestbook(**guestbook_in.model_dump())
    session.add(guest)
    session.commit()
    session.refresh(guest)
    return guest

# delete a specific entry in the guestbook
@router.delete("/guestbook/{entry_id}")
def delete_guestbook_entry(entry_id: Annotated[int, Path()], session: Session) -> Message:
    """
    Delete an item from the guestbook
    """
    guest = session.query(Guestbook).filter(Guestbook.id == entry_id).first()
    if not guest:
        raise HTTPException(status_code=404, detail="Guestbook entry not found")
    # TODO: add a conditional for checking current user id with the guestbook entry id relation
    session.delete(guest)
    session.commit()
    return Message(message="Guestbook entry deleted successfully")
    
    
    
