from pydantic import BaseModel

from core.reused_types import pydantic_types

from typing import Optional
from datetime import datetime


class UserData(BaseModel):
    first_name: pydantic_types.string64
    last_name: Optional[pydantic_types.string64] = None


class UserScheme(UserData):
    id: int
    created_at: datetime
    updated_at: datetime
