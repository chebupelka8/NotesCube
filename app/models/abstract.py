from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class AbstractModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(unique=True, primary_key=True, autoincrement=True)
