from typing import Optional, Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .abstract import AbstractModel
from core import string64, utc_creation_date, utc_updated_date


class NoteModel(AbstractModel):
    __tablename__ = "notes"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[string64]
    description: Mapped[Optional[str]]
    created_at: Mapped[utc_creation_date] 
    updated_at: Mapped[utc_updated_date]
