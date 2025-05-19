from core.database import DBBaseModel
from sqlalchemy import Column, String, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.groups_models import GroupsModel
 # Assumindo que esse é o nome correto

class CharactersModel(DBBaseModel):
    __tablename__ = "VDCharacters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    age = Column(Integer())
    height = Column(Float())
    role = Column(String(256))  # ex: vampiro, bruxo
    origin = Column(String(256))
    family = Column(String(256))  # NOVO
    description = Column(Text, nullable=True)
    image = Column(String(256), nullable=True)

    group_id = Column(Integer, ForeignKey("VDGroups.id"), nullable=True)  # NOVO
    group = relationship("GroupsModel", back_populates="characters")      # NOVO
