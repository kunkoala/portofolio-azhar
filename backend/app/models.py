from sqlmodel import Field, SQLModel, Column
from sqlalchemy import DateTime, func, text
from typing import Optional
import datetime


# shared properties
class GuestbookBase(SQLModel):
    created_by: str = Field(max_length=80)
    message: str = Field(max_length=80)

# properties to receive on item creation    
class GuestbookCreate(GuestbookBase):
    created_by: str = Field(min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=80)
    

# properties to return via API, id is required
class GuestbookPublic(GuestbookBase):
    id: int
    
    # remember to use datetime.datetime instead of datetime for the type hint
    created_at: datetime.datetime
    updated_at: datetime.datetime
    
    class Config:
        orm_mode = True


class Guests(SQLModel):
    data: list[GuestbookPublic]
    count: int
    

# database model
class Guestbook(GuestbookBase, table=True):
    __tablename__ = "guestbook"

    id: int | None = Field(default=None, primary_key=True)
    created_by: str = Field(max_length=80)
    message: str = Field(max_length=80)
    created_at: datetime.datetime = Field(sa_column=Column(DateTime, server_default=func.now()))
    updated_at: Optional[datetime.datetime] = Field(sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))
    
    
class Message(SQLModel):
    message: str


'''
Use Pydantic's orm_mode¶
Now, in the Pydantic models for reading, Item and User, add an internal Config class.

This Config class is used to provide configurations to Pydantic.

In the Config class, set the attribute orm_mode = True

Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
'''



