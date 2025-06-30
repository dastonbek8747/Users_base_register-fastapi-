from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas
from authx import AuthX, AuthXConfig
from db_connect import db_dependsy
from hash_password import hash_password, verify_password

router = APIRouter()

# AuthX konfiguratsiyasi
config = AuthXConfig()
config.JWT_SECRET_KEY = "my_secret_key"
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"  # ✅ to'g'rilandi
config.JWT_TOKEN_LOCATION = ["cookies"]  # yoki ["headers"] agar cookie emas bo‘lsa
token_auth = AuthX(config)


@router.post("/register", response_model=schemas.UserOut)
async def user_register(user: schemas.UserCreate, db: db_dependsy):
    # Email va username unikalmi?
    if db.query(models.Users).filter(models.Users.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    if db.query(models.Users).filter(models.Users.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    # Parolni hashlab bazaga saqlaymiz
    hashed_password = hash_password(user.password)
    new_user = models.Users(
        email=user.email,
        username=user.username,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Token yaratamiz
    token = token_auth.create_access_token(str(new_user.id))
    print(token)  # kerak bo‘lsa frontga cookie orqali yuboriladi

    return new_user


@router.post("/login", response_model=schemas.UserOut)
async def user_login(user: schemas.UserLogin, db: db_dependsy):
    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Email not registered")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Token yaratamiz
    token = token_auth.create_access_token(str(db_user.id))

    return db_user


@router.get("/user/{user_id}", response_model=schemas.UserOut)
async def get_user_by_id(user_id: int, db: db_dependsy):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/user", response_model=list[schemas.UserOut])
async def get_all_users(db: db_dependsy):
    return db.query(models.Users).all()
