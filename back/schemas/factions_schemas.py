from typing import Optional
from pydantic import BaseModel

class FactionsSchema(BaseModel): 
    id: Optional[int]
    name: str  # Nome da facção (por exemplo, Vampiros, Bruxas, Lobisomens, etc.)
    leader: str  # Líder da facção (pode ser o nome do personagem principal ou um líder da facção)
    hideout: str  # Refúgio ou local onde a facção se reúne ou habita (pode ser uma cidade ou local específico)
    symbol_image: str  # Uma imagem que representa a facção (logo, emblema, etc.)

    class Config:
        orm_mode = True
