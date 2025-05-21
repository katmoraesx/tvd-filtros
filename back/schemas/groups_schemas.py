from pydantic import BaseModel
from typing import Optional
from .characters_schemas import CharacterSchema


# 🔹 Schema de leitura
class GroupSchemaRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None  # mantém para poder ler e enviar na API

    class Config:
        orm_mode = True

# 🔹 Schema de criação
class GroupSchemaCreate(BaseModel):
    name: str
    description: Optional[str] = None  # mantém para receber na API, mas não salva no banco

# 🔹 Schema de atualização
class GroupSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None  # mantém para receber na API, mas não salva no banco
