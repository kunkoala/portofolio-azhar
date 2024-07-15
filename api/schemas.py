from pydantic import BaseModel

class GuestbookBase(BaseModel):
    name: str
    email: str
    message: str
    created_by: str
    
class GuestbookCreate(GuestbookBase):
    pass

'''
Use Pydantic's orm_mode¶
Now, in the Pydantic models for reading, Item and User, add an internal Config class.

This Config class is used to provide configurations to Pydantic.

In the Config class, set the attribute orm_mode = True

Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
'''
class Guestbook(GuestbookBase):
    id: int
    created_at: str
    updated_at: str
    
    class Config:
        orm_mode = True