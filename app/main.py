from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from contextlib import asynccontextmanager

from database import AbstractDataBase
from routers import users_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    await AbstractDataBase.create_all_tables()
    yield
    

app = FastAPI(
    title="NotesCube",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users_router)

@app.get("/home")
async def home():
    return {
        "status": 200
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)