# Scaffold

Minimum working plumbing: a FastAPI + SQLAlchemy backend and a Vite + React frontend,
wired together. No business logic — just enough to prove the stack boots end to end
before you build anything on top of it.

## Run it

**Backend** (http://localhost:8000):

```
cd backend
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend** (http://localhost:5173):

```
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — it should say `backend: ok, db: connected`. If it says
"backend unreachable," make sure uvicorn is still running on :8000.

## Database

Defaults to a local SQLite file (`backend/app.db`), created automatically on first run.
No Docker, no server to install. To point it at real Postgres instead, set
`DATABASE_URL` in `backend/.env` (see `backend/.env.example`) — `db.py` is
engine-agnostic, nothing else needs to change.

## Adding your own models

Add SQLAlchemy models to `backend/db.py` (or a new file imported by `main.py`). Tables
are created automatically on startup via `Base.metadata.create_all()` — no migrations
needed at this scope.
