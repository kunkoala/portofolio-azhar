from functools import lru_cache
from fastapi import FastAPI, Depends, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated

from .database import SessionLocal
from .models import Guestbook
from .config import settings
from pydantic import BaseModel, Field



app = FastAPI()

# Add CORS middleware, CORS middleware is used to allow cross-origin requests
# from the frontend to the backend API server.

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''CORS stands for Cross-Origin Resource Sharing. It is a mechanism that 
allows web browsers to securely make requests to a different domain than the 
one the web page originated from.

By default, web browsers enforce a security policy called the Same-Origin 
Policy, which restricts web pages from making requests to a different domain. 
This policy is in place to prevent malicious scripts from accessing sensitive 
data or performing unauthorized actions on behalf of the user.'''


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/hello")
async def read_root():
    return {"message": "Hello World! This API is now working yippie!"}


@lru_cache
def get_settings():
    return settings


@app.get("/info")
async def info(settings: Annotated[settings, Depends(get_settings)]):
    return {
        "app_name": settings.APP_NAME,
        "ENV (prod or dev)": settings.ENVIRONMENT,
        "DATABASE_ENV": str(settings.SQLALCHEMY_DATABASE_URI),
    }


@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Guestbook).all()


'''
TODO: Implement the following API endpoints for the guestbook:
1. Create a new entry in the guestbook
2. Read all entries in the guestbook
3. Read a specific entry in the guestbook
4. Update a specific entry in the guestbook
5. Delete a specific entry in the guestbook
'''


@app.get("/api/guestbook")
async def read_guestbook(db: Annotated[Session, Depends(get_db)]):
    return db.query(Guestbook).all()
