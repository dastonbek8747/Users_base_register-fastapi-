from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from fastapi import Depends
import os
from typing import Annotated

load_dotenv()

URL_DATABASE = os.getenv("DATABASE_URL")

engine = create_engine(URL_DATABASE)
localsession = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()


async def get_db():
    db = localsession()
    try:
        yield db
    finally:
        db.close()


db_dependsy = Annotated[localsession, Depends(get_db)]
