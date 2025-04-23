from core.base import DBBaseModel  # Base correta
from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class GroupsModel(DBBaseModel):
    __tablename__ = "VDGroups"  # Grupos como "Família Salvatore", "Bruxas", "Doppelgängers", etc.

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)  # Nome do grupo
    description = Column(Text, nullable=True)  # Breve descrição do grupo
    image = Column(String(256), nullable=True)  # Imagem representativa do grupo

    characters = relationship("CharactersModel", back_populates="group", lazy="selectin")


class CharactersModel(DBBaseModel):
    __tablename__ = "VDCharacters"  # Personagens principais

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)  # Nome do personagem
    description = Column(Text, nullable=True)  # Descrição do personagem
    image = Column(String(256), nullable=True)  # URL ou path da imagem do personagem
    group_id = Column(Integer, ForeignKey("VDGroups.id"))  # Chave estrangeira para o grupo

    group = relationship("GroupsModel", back_populates="characters", lazy="selectin")
