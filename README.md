# 👥 Users Base Register (FastAPI)

Foydalanuvchilarni ro'yxatdan o'tkazish uchun **FastAPI** backend. Parollar xavfsiz hash qilinadi, JWT autentifikatsiya qo'llanadi.

---

## ✨ Imkoniyatlar

- 📝 **Ro'yxatdan o'tish** va kirish
- 🔒 **Parol hashlash:** bcrypt (passlib)
- 🎫 **JWT token** autentifikatsiya
- 🐳 **Docker** qo'llab-quvvatlash (Dockerfile mavjud)
- 🔌 **REST API**

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **FastAPI** | REST API |
| **SQLAlchemy** | ORM |
| **passlib / bcrypt** | Parol hashlash |
| **Docker** | Konteynerizatsiya |

---

## ⚙️ O'rnatish

```bash
git clone https://github.com/dastonbek8747/Users_base_register-fastapi-.git
cd Users_base_register-fastapi-
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

`.env` fayl yarating:

```env
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=<random_secret>
```

> 🔒 `.env` git'ga qo'shilmaydi.

---

## ▶️ Ishga tushirish

```bash
cd app && python main.py
```

**Docker bilan:**

```bash
docker build -t users-api .
docker run -p 8000:8000 users-api
```

---

## 📁 Loyiha tuzilishi

```
Users_base_register-fastapi-/
├── app/
│   ├── main.py           # FastAPI app
│   ├── routers.py        # Endpointlar
│   ├── models.py         # Modellar
│   ├── schemas.py        # Sxemalar
│   ├── db_connect.py     # DB ulanishi
│   └── hash_password.py  # Parol hashlash
├── Dockerfile
└── requirements.txt
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
