# API
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
import uvicorn

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/hello")
def read_root():
    return {"message": "Hello World! This API is now working yippie!"}

@app.get("/")
def home(db: Session = Depends(get_db)):
    return {"message": "Welcome to the site! DB is also loaded"}