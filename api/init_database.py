from .database import Base, engine, SessionLocal
from .models import Guestbook

def init_database():
    Base.metadata.create_all(bind=engine)
    print("Database initialized")
    return True

def add_values():
    db = SessionLocal()
    guest_1 = Guestbook(name="John Doe", email="test@mail.de", message="Hello World!", created_by="John Doe")
    db.add(guest_1)
    db.commit()
    db.close()
    
    print(f"Values added: {guest_1}")