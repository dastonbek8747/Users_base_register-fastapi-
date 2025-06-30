from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email :EmailStr
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    username: str
    email : EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
