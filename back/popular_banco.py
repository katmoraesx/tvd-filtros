from core.configs import settings
from core.database import engine
from models.characters_models import CharactersModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
import asyncio

Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def popular():
    async with Session() as session:
        personagem1 = CharactersModel(
            name="Elena Gilbert",
            age=18,
            height=1.65,
            role="Protagonista",
            origin="Mystic Falls",
            description="Estudante envolvida com vampiros",
            image="https://link-da-imagem/elena.jpg"
        )

        personagem2 = CharactersModel(
            name="Damon Salvatore",
            age=170,
            height=1.80,
            role="Vampiro",
            origin="Mystic Falls",
            description="Irmão de Stefan, personalidade sarcástica",
            image="https://link-da-imagem/damon.jpg"
        )

        personagem3 = CharactersModel(
            name="Stefan Salvatore",
            age=170,
            height=1.78,
            role="Vampiro",
            origin="Mystic Falls",
            description="Irmão de Damon, mais calmo e racional",
            image="https://link-da-imagem/stefan.jpg"
        )

        session.add_all([personagem1, personagem2, personagem3])
        await session.commit()

    print("Banco populado com sucesso!")

if __name__ == "__main__":
    asyncio.run(popular())
