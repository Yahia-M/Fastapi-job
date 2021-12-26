from sqlalchemy import create_engine, engine
from sqlalchemy.orm import session, sessionmaker

from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db() -> Generator:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()