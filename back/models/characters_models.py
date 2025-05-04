from core.configs import settings  # Base correta
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Float
from sqlalchemy.orm import relationship


class CharactersModel(settings.DBBaseModel):
    __tablename__ = "VDCharacters"  # Personagens principais

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)  # Nome do personagem
    age = Column(Integer())
    height = Column(Float())
    role = Column(String(256))
    origin = Column(String(256))
    description = Column(Text, nullable=True)  # Descrição do personagem
    image = Column(String(256), nullable=True)  # URL ou path da imagem do personagem
