from core.configs import settings
from sqlalchemy import Column, String, Integer, Float

class PlayersModel(settings.DBBaseModel):
    __tablename__ = "NBAPlayers"

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    name: str = Column(String(256))
    age: int = Column(Integer())
    height: float = Column(Float())
    position: str = Column(String(256))
    time: str = Column(String(256))
    country: str = Column(String(256))
    image: str = Column(String(256))