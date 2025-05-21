from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Optional, List

class CharacterSchema(BaseModel):
    id: Optional[int]
    name: str
    age: int
    height: float
    role: str
    origin: str
    description: str
    image: str
    group_id: Optional[int]

    class Config:
        orm_mode = True

class GroupSchemaRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    characters: List[CharacterSchema] = Field(default_factory=list)  # evita problema com lista mutável

    class Config:
        orm_mode = True

class GroupSchemaCreate(BaseModel):
    name: str
    description: Optional[str] = None

class GroupSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
