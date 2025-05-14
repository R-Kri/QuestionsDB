from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create an SQLite DB (local file)
engine = create_engine('sqlite:///jee_questions.db')

# Create tables
Base.metadata.create_all(engine)

# Create a session to interact with DB
SessionLocal = sessionmaker(bind=engine)

def get_db_session():
    """Get a new database session"""
    return SessionLocal()