from pydantic import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    DB_URL: str = "mysql+aiomysql://root:senai@127.0.0.1:3306/thevampirediaries"  # novo nome de banco


    DBBaseModel = declarative_base()

class Config:
    case_sensitive = True
    env_file = ".env"

# Instância das configurações
settings = Settings()

# Declarative base global para os models
