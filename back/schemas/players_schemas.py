from typing import Optional
from pydantic import BaseModel
from schemas.teams_schemas import TeamsSchema


class PlayersSchema(BaseModel):
    id: Optional[int]
    name: str
    age: int
    height: float
    position: str
    country: str
    image: str
    team_id: Optional[int]  

    class Config:
        orm_mode = True

class PlayersTeamsSchema(PlayersSchema):
    
    class Config:
        orm_mode = True