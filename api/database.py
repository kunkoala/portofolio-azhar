import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

env = os.getenv('ENV', 'development')
if env == 'development':
    load_dotenv('.env.development.local')
elif env == 'production':
    load_dotenv('.env.production.local')
    
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL_DEV') if env == 'development' else os.getenv('DATABASE_URL_PROD')


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()