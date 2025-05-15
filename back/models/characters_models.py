from core.configs import DBBaseModel  # IMPORTA DBBaseModel DIRETO, NÃO settings
from sqlalchemy import Column, String, Integer, Text, Float

class CharactersModel(DBBaseModel):
    __tablename__ = "VDCharacters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    age = Column(Integer())
    height = Column(Float())
    role = Column(String(256))
    origin = Column(String(256))
    description = Column(Text, nullable=True)
    image = Column(String(256), nullable=True)
