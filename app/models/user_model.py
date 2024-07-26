from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from .abstract import AbstractModel

from core import utc_creation_date, string64


class UserModel(AbstractModel):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(unique=True)
    first_name: Mapped[string64]
    last_name: Mapped[Optional[string64]] 
    created_at: Mapped[utc_creation_date] 
