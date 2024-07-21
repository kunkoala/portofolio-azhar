import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# determine the environment, default is development
env = os.getenv('ENV', default='development')

# load the environment variables, check whether it's development or production
if env == 'development':
    load_dotenv('.env.development.local')
elif env == 'production':
    load_dotenv('.env.production.local')
    
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

print(f"SQLALCHEMY_DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
