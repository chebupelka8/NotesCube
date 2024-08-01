from pydantic import BaseModel
from datetime import datetime


class NoteData(BaseModel):
    title: str
    description: str
    content: str


class Note(NoteData):
    id: int
    created_at: datetime
    updated_at: datetime
    

