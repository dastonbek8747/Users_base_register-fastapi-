# Users Base Register (FastAPI)

Foydalanuvchilarni ro'yxatdan o'tkazish uchun FastAPI backend: autentifikatsiya va parol xeshlash.

## Imkoniyatlar

- Ro'yxatdan o'tish / kirish
- Parollarni xeshlash (bcrypt/argon2)
- PostgreSQL + SQLAlchemy
- Docker qo'llab-quvvatlanadi

## O'rnatish

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Sozlash

```bash
cp .env.example .env
# .env ichida DATABASE_URL ni to'ldiring
```

## Ishga tushirish

```bash
uvicorn app.main:app --reload
```

yoki Docker bilan:

```bash
docker build -t users-base .
docker run -p 8000:8000 users-base
```

## Litsenziya

MIT
