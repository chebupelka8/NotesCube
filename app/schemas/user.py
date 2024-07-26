from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
