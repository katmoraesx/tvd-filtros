from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List
from .characters_schemas import CharacterSchema


# 🔹 Schema para leitura (inclui personagens)
class GroupSchemaRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    characters: List[CharacterSchema] = Field(default_factory=list)  # Lista de personagens no grupo

    class Config:
        orm_mode = True


# 🔹 Schema para criação
class GroupSchemaCreate(BaseModel):
    name: str
    description: Optional[str] = None


# 🔹 Schema para atualização
class GroupSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
