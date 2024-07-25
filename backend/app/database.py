from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URI
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(str(SQLALCHEMY_DATABASE_URL))

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)
