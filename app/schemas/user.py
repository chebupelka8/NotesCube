from pydantic import BaseModel

from typing import Optional


class CreateUser(BaseModel):
    first_name: str
    last_name: Optional[str] = None


class UserScheme(CreateUser):
    id: int
