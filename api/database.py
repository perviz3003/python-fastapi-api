from .config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://{}:{}@{}:{}/{}'.format(
        settings.db_user,
        settings.db_user_password,
        settings.db_host,
        settings.db_port,
        settings.db_name
    )
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def dbc():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
