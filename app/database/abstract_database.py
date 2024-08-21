from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fastapi import HTTPException

from models import AbstractModel
from core import DATABASE_URL


class AbstractDataBase:
    engine = create_async_engine(DATABASE_URL, echo=False) # type: ignore
    session = async_sessionmaker(engine)

    @classmethod
    async def run_metadata_method(cls, method: str) -> None:
        if not hasattr(AbstractModel.metadata, method):
            raise HTTPException(status_code=500, detail=f"Method '{method}' not found.")

        async with cls.engine.connect() as connection:
            await connection.run_sync(
                getattr(AbstractModel.metadata, method)
            )
            
    @classmethod
    async def create_all_tables(cls) -> None:
        await cls.run_metadata_method("create_all")

    @classmethod
    async def drop_all_tables(cls) -> None:
        await cls.run_metadata_method("drop_all")
