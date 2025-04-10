from typing import Optional
from pydantic import BaseModel as SCBaseModel

class PlayersSchema(SCBaseModel):
    id: Optional[int] = None
    name: str
    age: int
    height: float
    position: str
    time: str
    country: str
    image: str

class Config:
    orm_mode = True