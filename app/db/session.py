from sqlalchemy import create_engine

from sqlalchemy.orm import (
    sessionmaker,
)

DATABASE_URL = (
    "mysql+pymysql://root:123$@localhost/pygate"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
