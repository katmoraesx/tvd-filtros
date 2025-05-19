from pydantic import BaseModel
from typing import Optional

# 🔹 Schema de leitura
class GroupSchemaRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

# 🔹 Schema de criação
class GroupSchemaCreate(BaseModel):
    name: str
    description: Optional[str] = None

# 🔹 Schema de atualização
class GroupSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
