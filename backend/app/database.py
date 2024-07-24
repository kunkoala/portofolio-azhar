import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.config import settings

# Load environment variables from .env file
load_dotenv(f".env.{settings.ENV}.local")

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
