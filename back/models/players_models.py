from core.configs import settings
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class TeamsModel(settings.DBBaseModel):
    __tablename__ = "NBATeams"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))
    city: str = Column(String(256))
    arena: str = Column(String(256))
    image_arena: str = Column(String(256))

    players = relationship("PlayersModel", back_populates="team", lazy="selectin")


class PlayersModel(settings.DBBaseModel):
    __tablename__ = "NBAPlayers"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))
    age: int = Column(Integer())
    height: float = Column(Float())
    position: str = Column(String(256))
    country: str = Column(String(256))
    image: str = Column(String(256))
    team_id: int = Column(Integer, ForeignKey("NBATeams.id"))  

    team = relationship("TeamsModel", back_populates="players", lazy="selectin")