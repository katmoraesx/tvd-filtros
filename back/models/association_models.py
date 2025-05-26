# models/association.py

from sqlalchemy import Table, Column, Integer, ForeignKey
from core.database import DBBaseModel

characters_groups = Table(
    "characters_groups",
    DBBaseModel.metadata,
    Column("character_id", Integer, ForeignKey("VDCharacters.id")),
    Column("group_id", Integer, ForeignKey("VDGroups.id"))
)
