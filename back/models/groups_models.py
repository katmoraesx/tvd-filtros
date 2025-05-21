from core.database import DBBaseModel
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

class GroupsModel(DBBaseModel):
    __tablename__ = "VDGroups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)  # Opcional

    characters = relationship("CharactersModel", back_populates="group")
