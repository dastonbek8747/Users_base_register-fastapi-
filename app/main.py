from fastapi import FastAPI
from routers import router
import uvicorn
from db_connect import engine, Base

app = FastAPI()
app.include_router(router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "Hello from Docker"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
