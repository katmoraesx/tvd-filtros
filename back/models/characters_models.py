from core.configs import settings
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

class GroupsModel(settings.DBBaseModel):
    __tablename__ = "VDGroups"  # Grupos como "Família Salvatore", "Bruxas", "Doppelgängers", etc.

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))  # Nome do grupo
    description: str = Column(Text())  # Breve descrição do grupo
    image: str = Column(String(256))  # Imagem representativa do grupo

    characters = relationship("CharactersModel", back_populates="group", lazy="selectin")


class CharactersModel(settings.DBBaseModel):
    __tablename__ = "VDCharacters"  # Personagens principais

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))  # Nome do personagem
    description: str = Column(Text())  # Descrição do personagem
    image: str = Column(String(256))  # URL ou path da imagem do personagem
    group_id: int = Column(Integer, ForeignKey("VDGroups.id"))  # Chave estrangeira para o grupo

    group = relationship("GroupsModel", back_populates="characters", lazy="selectin")
