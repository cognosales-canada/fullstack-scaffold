from __future__ import annotations

import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# Defaults to a local SQLite file — zero setup, no Docker, no server process to install.
# Swap to a real Postgres URL (e.g. postgresql+psycopg2://user:pass@localhost:5432/db)
# by setting DATABASE_URL — everything below is engine-agnostic.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

# SQLite needs this for use across threads (FastAPI's threadpool); Postgres ignores it.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
