from typing import Optional
from pydantic import BaseModel
from schemas.factions_schemas import FactionsSchema  # Corrigido: removido 'back.'

class CharacterSchema(BaseModel):  # Renomeado para CharactersSchema
    id: Optional[int]
    name: str
    age: int
    height: float  # Pode manter ou remover dependendo da necessidade, se não for relevante no contexto de personagens.
    role: str  # "position" alterado para "role", como vampiro, bruxo, etc.
    origin: str  # "country" alterado para "origin", representando o lugar de origem no universo de The Vampire Diaries
    description: str
    image: str
    group_id: Optional[int]  # Alterado de "team_id" para "faction_id" para representar a facção no universo de "The Vampire Diaries"

    class Config:
        orm_mode = True

class CharactersFactionsSchema(CharacterSchema):  # Renomeado para CharactersFactionsSchema
    class Config:
        orm_mode = True
