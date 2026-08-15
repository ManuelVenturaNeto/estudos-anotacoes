from typing import Optional
from pydantic import BaseModel



# Pydantic models
class Pet(BaseModel):
    id: Optional[int] = None
    name: str
    type: str
    age: Optional[int] = None


class PetUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    age: Optional[int] = None









