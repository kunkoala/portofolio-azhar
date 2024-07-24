import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = os.getenv('ENV', default='development')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    
    class Config:
        env_file = f".env.{os.getenv('ENV','development')}.local"

settings = Settings()