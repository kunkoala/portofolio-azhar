import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from dotenv import load_dotenv

from ..database import Base
from ..main import app, get_db

# determine the environment, default is development
env = os.getenv('ENV', default='development')

# load the environment variables, check whether it's development or production
if env == 'development':
    load_dotenv('.env.development.local')
elif env == 'production':
    load_dotenv('.env.production.local')
    
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

# debug the SQLALCHEMY_DATABASE_URL
print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL, poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_guestbook():
    
    # write the code for the test here
    pass
