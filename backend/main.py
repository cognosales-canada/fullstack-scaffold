from __future__ import annotations

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from db import Base, engine, get_db

app = FastAPI(title="Scaffold API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    # Creates tables for any models you add to db.py (or a new file imported here).
    # Fine for a throwaway app — no migrations needed at this scope.
    Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text("SELECT 1"))
    return {"status": "ok", "db": "connected"}


# Add your own routes below (or in a new file, imported and registered with
# app.include_router(...) — your call).
