from core.database import engine
from models.characters_models import CharactersModel
from models.groups_models import GroupsModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
import asyncio

Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def popular():
    async with Session() as session:
        # Grupos
        grupo1 = GroupsModel(name="Vampiros")
        grupo2 = GroupsModel(name="Lobos")
        grupo3 = GroupsModel(name="Bruxas")
        grupo4 = GroupsModel(name="Caçadores")
        grupo5 = GroupsModel(name="Humanos")

        session.add_all([grupo1, grupo2, grupo3, grupo4, grupo5])
        await session.flush()

        # Personagens
        personagens = [
            CharactersModel(
                name="Elena Gilbert", age=18, height=1.65, role="Protagonist",
                origin="Mystic Falls",
                description="High school student caught in the world of vampires.",
                image="https://link-da-imagem/elena.jpg",
                groups=[grupo1, grupo5]
            ),
            CharactersModel(
                name="Damon Salvatore", age=170, height=1.80, role="Vampire",
                origin="Mystic Falls",
                description="Stefan's brother, known for his sarcastic and unpredictable nature.",
                image="https://link-da-imagem/damon.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Stefan Salvatore", age=170, height=1.78, role="Vampire",
                origin="Mystic Falls",
                description="Damon's brother, calm and rational with a strong moral compass.",
                image="https://link-da-imagem/stefan.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Bonnie Bennett", age=18, height=1.64, role="Witch",
                origin="Mystic Falls",
                description="Powerful witch and close friend of Elena.",
                image="https://link-da-imagem/bonnie.jpg",
                groups=[grupo3]
            ),
            CharactersModel(
                name="Caroline Forbes", age=18, height=1.70, role="Vampire",
                origin="Mystic Falls",
                description="Former cheerleader turned into a responsible vampire.",
                image="https://link-da-imagem/caroline.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Matt Donovan", age=18, height=1.83, role="Human",
                origin="Mystic Falls",
                description="Loyal friend and former boyfriend of Elena.",
                image="https://link-da-imagem/matt.jpg",
                groups=[grupo5]
            ),
            CharactersModel(
                name="Klaus Mikaelson", age=1000, height=1.85, role="Original Hybrid",
                origin="Mystic Falls",
                description="The first hybrid, both vampire and werewolf.",
                image="https://link-da-imagem/klaus.jpg",
                groups=[grupo1, grupo2]
            ),
            CharactersModel(
                name="Rebekah Mikaelson", age=1000, height=1.72, role="Original Vampire",
                origin="Mystic Falls",
                description="Sister of Klaus, emotional and loyal.",
                image="https://link-da-imagem/rebekah.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Tyler Lockwood", age=18, height=1.82, role="Werewolf/Hybrid",
                origin="Mystic Falls",
                description="Former athlete who becomes a werewolf.",
                image="https://link-da-imagem/tyler.jpg",
                groups=[grupo2]
            ),
            CharactersModel(
                name="Jeremy Gilbert", age=17, height=1.78, role="Hunter",
                origin="Mystic Falls",
                description="Elena’s younger brother who becomes a vampire hunter.",
                image="https://link-da-imagem/jeremy.jpg",
                groups=[grupo4]
            ),
            CharactersModel(
                name="Alaric Saltzman", age=35, height=1.88, role="Vampire Hunter",
                origin="Mystic Falls",
                description="History teacher and mentor to Elena and her friends.",
                image="https://link-da-imagem/alaric.jpg",
                groups=[grupo4]
            ),
            CharactersModel(
                name="Enzo St. John", age=100, height=1.82, role="Vampire",
                origin="England",
                description="Damon's old friend from captivity with a charming yet dangerous side.",
                image="https://link-da-imagem/enzo.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Kai Parker", age=22, height=1.80, role="Witch",
                origin="Portland",
                description="Powerful and psychopathic siphoner witch from the Gemini coven.",
                image="https://link-da-imagem/kai.jpg",
                groups=[grupo3]
            ),
            CharactersModel(
                name="Lorenzo St. John", age=100, height=1.80, role="Vampire",
                origin="Unknown",
                description="Also known as Enzo, independent and loyal with strong feelings for Bonnie.",
                image="https://link-da-imagem/enzo2.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Lexi Branson", age=350, height=1.75, role="Vampire",
                origin="Chicago",
                description="Stefan’s best friend who helps him stay on the right path.",
                image="https://link-da-imagem/lexi.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Jenna Sommers", age=30, height=1.68, role="Human",
                origin="Mystic Falls",
                description="Elena’s aunt and guardian after her parents’ death.",
                image="https://link-da-imagem/jenna.jpg",
                groups=[grupo5]
            ),
            CharactersModel(
                name="Vicki Donovan", age=17, height=1.68, role="Vampire",
                origin="Mystic Falls",
                description="Matt's sister who becomes one of the first vampires in the series.",
                image="https://link-da-imagem/vicki.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Logan Fell", age=35, height=1.80, role="Vampire",
                origin="Mystic Falls",
                description="News reporter turned into a vampire with selfish motives.",
                image="https://link-da-imagem/logan.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Rose", age=500, height=1.75, role="Vampire",
                origin="England",
                description="Centuries-old vampire who helps Elena and the Salvatores.",
                image="https://link-da-imagem/rose.jpg",
                groups=[grupo1]
            ),
            CharactersModel(
                name="Liz Forbes", age=45, height=1.70, role="Sheriff",
                origin="Mystic Falls",
                description="Caroline’s mother and the town sheriff.",
                image="https://link-da-imagem/liz.jpg",
                groups=[grupo5]
            ),
            CharactersModel(
                name="Mason Lockwood", age=35, height=1.85, role="Werewolf",
                origin="Mystic Falls",
                description="Tyler’s uncle who helps him understand his curse.",
                image="https://link-da-imagem/mason.jpg",
                groups=[grupo2]
            ),
        ]

        session.add_all(personagens)
        await session.commit()

    print("Banco populado com sucesso!")

if __name__ == "__main__":
    asyncio.run(popular())
