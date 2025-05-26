# models/groups_models.py

from core.database import DBBaseModel
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from models.association_models import characters_groups


class GroupsModel(DBBaseModel):
    __tablename__ = "VDGroups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)

    characters = relationship("CharactersModel", secondary=characters_groups, back_populates="groups")
