from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.settings import DATABASE_URL


Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
