from typing import Optional, TYPE_CHECKING

from sqlalchemy.orm import Mapped
from .abstract import AbstractModel

from core import utc_creation_date, string64


class UserModel(AbstractModel):
    __tablename__ = "users"

    first_name: Mapped[string64]
    last_name: Mapped[Optional[string64]] 
    created_at: Mapped[utc_creation_date] 
