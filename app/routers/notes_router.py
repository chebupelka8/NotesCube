from typing import Annotated

from fastapi import APIRouter, Depends
from repositories import NotesRepository

from schemas import NoteData

from core.reused_types import pydantic_types


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.post("/new")
async def create_note(note: Annotated[NoteData, Depends()]):
    new_note = await NotesRepository.add_note(note)

    return {
        "status": 200,
        "note": new_note
    }


@router.delete("/delete")
async def delete_note(note_id: pydantic_types.id_range):
    deleted = await NotesRepository.remove_note_by_id(note_id)

    return {
        "status": 200,
        "deleted": deleted
    }


@router.post("/search")
async def search_note(query: str):
    ...


@router.get("/{id}")
async def get_note_by_id(id: pydantic_types.id_range):
   return await NotesRepository.get_note_by_id_as_scheme(id)
