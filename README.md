# FastAPI User Auth (JWT)

> Registration and login API with JWT access tokens and hashed passwords. FastAPI + PostgreSQL + Docker.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)


## Features

- User registration with email validation.
- Password hashing before storage.
- Login returns a signed JWT access token.
- Dockerfile for a reproducible build.
- Routers split by concern for a clean layout.

## Tech Stack

| Layer | Technology |
|---|---|
| API | FastAPI, Uvicorn |
| Auth | PyJWT, password hashing |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Packaging | Docker |

## Quick Start

```bash
git clone https://github.com/dastonbek8747/fastapi-user-auth-jwt.git
cd fastapi-user-auth-jwt
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # set DATABASE_URL and SECRET_KEY
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs.

## Environment variables

| Variable | Meaning |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string. |
| `SECRET_KEY` | Secret used to sign JWTs. Use a long random value. |

## Project Structure

```
app/
├── main.py           # FastAPI app
├── routers.py        # auth + user routes
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── hash_password.py  # password hashing helpers
└── db_connect.py     # engine, session, Base
Dockerfile
```

## Security Notes

- `.env` is not committed. Copy `.env.example` and fill it in.
- Never reuse the example secret. Generate one with `python -c "import secrets; print(secrets.token_urlsafe(48))"`.

## License

MIT © 2026 Doston Sultonov.
