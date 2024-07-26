from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from models import AbstractModel
from core import DATABASE_URL


class AbstractDataBase:
    engine = create_async_engine(DATABASE_URL, echo=True) # type: ignore
    session = async_sessionmaker(engine)

    @classmethod
    async def create_all_tables(cls) -> None:
        async with cls.engine.connect() as connection:
            print(AbstractModel.metadata.tables)
            await connection.run_sync(
                AbstractModel.metadata.create_all
            )
