# API
import datetime
from fastapi import FastAPI, Depends, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from .init_database import init_database, add_values
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Guestbook
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

# Add CORS middleware, CORS middleware is used to allow cross-origin requests from the frontend to the backend API server. 

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

'''
CORS stands for Cross-Origin Resource Sharing. It is a mechanism that allows web browsers to securely make requests to a different domain than the one the web page originated from.

By default, web browsers enforce a security policy called the Same-Origin Policy, which restricts web pages from making requests to a different domain. This policy is in place to prevent malicious scripts from accessing sensitive data or performing unauthorized actions on behalf of the user.
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/hello")
async def read_root():
    return {"message": "Hello World! This API is now working yippie!"}

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Guestbook).all()

@app.get("/api/init/database")
async def init_db(db: Annotated[Session, Depends(get_db)]):
    init_database()
    add_values()
    return db.query(Guestbook).all()

