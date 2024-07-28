from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

'''
Use Pydantic's orm_mode¶
Now, in the Pydantic models for reading, Item and User, add an internal Config class.

This Config class is used to provide configurations to Pydantic.

In the Config class, set the attribute orm_mode = True

Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
'''

# shared properties
class GuestbookBase(BaseModel):
    created_by: str = Field(max_length=80)
    message: str = Field(max_length=80)

# properties to receive on item creation    
class GuestbookCreate(GuestbookBase):
    created_by: str = Field(min_length=1, max_length=80)
    message: str = Field(min_length=1, max_length=80)
    

# properties to return via API, id is required
class GuestbookPublic(GuestbookBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class Guests(BaseModel):
    data: list[GuestbookPublic]
    count: int
    

class Message(BaseModel):
    message: str