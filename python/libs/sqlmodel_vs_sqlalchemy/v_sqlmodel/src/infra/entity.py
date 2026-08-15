from typing import Optional
from sqlmodel import SQLModel, Field


class Pets(SQLModel, table=True):

    id: Optional[int] = Field(primary_key=True, index=True)
    name: str
    type: str
    age: Optional[int] = None



