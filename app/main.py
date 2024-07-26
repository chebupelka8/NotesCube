from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager

from database import DataBase
from routers import users_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    await DataBase.create_all_tables()
    yield
    

app = FastAPI(
    title="NotesCube",
    lifespan=lifespan
)


app.include_router(users_router)

@app.get("/home")
async def home():
    return {
        "status": 200
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)