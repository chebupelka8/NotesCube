from pydantic import BaseModel

from typing import Optional


class UserData(BaseModel):
    first_name: str
    last_name: Optional[str] = None


class UserScheme(UserData):
    id: int
