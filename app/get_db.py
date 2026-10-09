from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from app.Settings import Settings, get_settings
from sqlalchemy.ext.declarative import declarative_base


Settings=get_settings()
engine=create_engine(Settings.DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)