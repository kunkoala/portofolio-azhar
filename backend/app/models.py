from sqlmodel import Field, SQLModel, Column
from sqlalchemy import DateTime, func, text
import datetime

"""
The GuestbookBase model is a shared model that contains the common properties of the GuestbookCreate and GuestbookPublic models.
"""
# shared properties
class GuestbookBase(SQLModel):
    created_by: str = Field(min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=255)

# properties to receive on item creation    
class GuestbookCreate(GuestbookBase):
    # TODO: later on, use the user.id and user.username as the created_by
    pass
    

# properties to return via API, id, created_at and updated_at is required
class GuestbookPublic(GuestbookBase):
    id: int
    
    # remember to use datetime.datetime instead of datetime for the type hint
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Guests(SQLModel):
    data: list[GuestbookPublic]
    count: int
    

# database model
class Guestbook(GuestbookBase, table=True):
    __tablename__ = "guestbook"

    """
    the id, created_at, and updated_at are not required in the GuestbookBase model, since they are handled by the database. 
    
    The default values in the python model will be set to None, and the database will handle the default values for the created_at and updated_at fields.
    """
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime.datetime | None = Field(default=None, sa_column=Column(DateTime, server_default=func.now(), nullable=False))
    updated_at: datetime.datetime | None = Field(default=None, sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))
    
    
class Message(SQLModel):
    message: str



