from pydantic import BaseModel
from typing import Optional

class CharacterSchema(BaseModel):
    id: Optional[int]
    name: str
    age: int
    height: float
    role: str
    origin: str
    description: str
    image: str
    group_id: Optional[int] = None

    class Config:
        orm_mode = True


class CharacterCreateSchema(BaseModel):
    name: str
    age: int
    height: float
    role: str
    origin: str
    description: str
    image: str
    group_id: Optional[int] = None
