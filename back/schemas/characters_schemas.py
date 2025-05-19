from pydantic import BaseModel
from typing import Optional
class CharacterSchema(BaseModel):
    id: Optional[int]
    name: str
    age: int
    height: float
    role: str
    origin: str
    family: str  # NOVO
    description: str
    image: str
    group_id: Optional[int]  # NOVO

    class Config:
        orm_mode = True
