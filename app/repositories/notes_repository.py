from database import AbstractDataBase


class NotesRepository(AbstractDataBase):

    @classmethod
    async def add_note(cls):
        ...
