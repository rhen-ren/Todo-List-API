from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///todolist.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)
Base = declarative_base()