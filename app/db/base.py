from sqlalchemy.orm import declarative_base
from app.db.database import engine

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)
