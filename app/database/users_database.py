from .database import DataBase


class UsersDataBase(DataBase):

    @classmethod
    async def add_user(cls) -> None:
        ...
