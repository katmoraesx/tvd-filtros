from core.database import DBBaseModel
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

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

    group_id = Column(Integer, ForeignKey("VDGroups.id"), nullable=True)
    group = relationship("GroupsModel", back_populates="characters")
