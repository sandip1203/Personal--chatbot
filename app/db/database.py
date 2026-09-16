from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import db_settings

engine = create_engine(db_settings.DATABASE_URL,
                       connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()