from fastapi import APIRouter
from repositories import NotesRepository


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


# @router.post("/new")
# async def create_note()
