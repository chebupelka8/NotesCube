from sqlalchemy import String
from sqlalchemy.orm import mapped_column

from datetime import datetime, UTC
from typing import Annotated

from pydantic import Field


type string256 = Annotated[str, mapped_column(String(256))]
type string64 = Annotated[str, mapped_column(String(64))]

type utc_creation_date = Annotated[
    datetime, mapped_column(default=lambda: datetime.now(UTC))
]

type utc_updated_date = Annotated[
    datetime, 
    mapped_column(onupdate=lambda: datetime.now(UTC), default=lambda: datetime.now(UTC))
]
