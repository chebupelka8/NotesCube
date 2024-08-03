from database import DataBase

from typing import Union, NoReturn

from schemas import NoteData, NoteScheme
from models import NoteModel

from core import require_return_else_HTTPException 


class NotesRepository(DataBase):

    @classmethod
    async def add_note(cls, note: NoteData) -> NoteScheme:
        result = await cls.add_something_orm(NoteModel, **note.model_dump())
        return NoteScheme(**result)
    
    @classmethod
    @require_return_else_HTTPException("Note not found.")
    async def remove_note_by_id(cls, note_id: int) -> Union[NoReturn, NoteScheme]:  # type: ignore
        if (target := await cls.get_by_id(NoteModel, note_id)) is not None:
            result = await cls.remove_something_orm(target)
            return NoteScheme(**result)
    
    @classmethod
    @require_return_else_HTTPException("Note not found.")
    async def get_note_by_id_as_scheme(cls, note_id: int) -> Union[NoReturn, NoteScheme]:  # type: ignore
        if (returning := await cls.get_by_id_as_scheme(NoteModel, note_id, NoteScheme)):
            return returning
