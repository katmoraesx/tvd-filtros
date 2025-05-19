from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.configs import DBBaseModel

class GroupsModel(DBBaseModel):
    __tablename__ = "VDGroups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    characters = relationship("CharactersModel", back_populates="group")
