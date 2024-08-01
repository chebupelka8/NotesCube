from pydantic import BaseModel

from typing import Optional
from datetime import datetime


class UserData(BaseModel):
    first_name: str
    last_name: Optional[str] = None


class UserScheme(UserData):
    id: int
    created_at: datetime
    updated_at: datetime
