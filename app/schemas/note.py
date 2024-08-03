from pydantic import BaseModel
from datetime import datetime

from core.reused_types import pydantic_types

from typing import Optional


class NoteData(BaseModel):
    user_id: pydantic_types.id_range
    title: pydantic_types.string64
    description: Optional[pydantic_types.string256] = None
    content: Optional[str] = None


class NoteScheme(NoteData):
    id: pydantic_types.id_range
    created_at: datetime
    updated_at: datetime
    

