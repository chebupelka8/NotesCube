from sqlalchemy.orm import Mapped, mapped_column
from .abstract import AbstractModel


class UserModel(AbstractModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
