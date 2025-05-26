# models/characters_models.py

from core.database import DBBaseModel
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from models.association_models import characters_groups


class CharactersModel(DBBaseModel):
    __tablename__ = "VDCharacters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    age = Column(Integer, nullable=True)
    height = Column(Float, nullable=True)
    role = Column(String(256), nullable=True)
    origin = Column(String(256), nullable=True)
    description = Column(Text, nullable=True)
    image = Column(String(256), nullable=True)

    groups = relationship("GroupsModel", secondary=characters_groups, back_populates="characters")
