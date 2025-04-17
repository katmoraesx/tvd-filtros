from typing import Optional
from pydantic import BaseModel


class TeamsSchema(BaseModel):
    id: Optional[int]
    name: str
    city: str
    arena: str
    image_arena: str

    class Config:
        orm_mode = True
