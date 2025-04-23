from typing import Optional
from pydantic import BaseModel
from back.schemas.factions_schemas import FactionsSchema  # Alterado para importar o novo schema de facções, se necessário

class CharactersSchema(BaseModel):  # Renomeado para CharactersSchema
    id: Optional[int]
    name: str
    age: int
    height: float  # Pode manter ou remover dependendo da necessidade, se não for relevante no contexto de personagens.
    role: str  # "position" alterado para "role", como vampiro, bruxo, etc.
    origin: str  # "country" alterado para "origin", representando o lugar de origem no universo de The Vampire Diaries
    image: str
    faction_id: Optional[int]  # Alterado de "team_id" para "faction_id" para representar a facção no universo de "The Vampire Diaries"

    class Config:
        orm_mode = True

class CharactersFactionsSchema(CharactersSchema):  # Renomeado para CharactersFactionsSchema
    class Config:
        orm_mode = True
