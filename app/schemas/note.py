from pydantic import BaseModel
from datetime import datetime

from core.reused_types import pydantic_types


class NoteData(BaseModel):
    title: pydantic_types.string64
    description: pydantic_types.string256
    content: str


class Note(NoteData):
    id: int
    created_at: datetime
    updated_at: datetime
    

