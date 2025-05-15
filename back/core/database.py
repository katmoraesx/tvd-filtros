from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncEngine = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

DBBaseModel = declarative_base()  # aqui você cria a base declarativa
