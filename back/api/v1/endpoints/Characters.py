from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.characters_models import CharactersModel  # Correção aqui
from schemas.characters_schemas import CharacterSchema 
from core.deps import get_session

router = APIRouter(
    prefix="/api/v1/characters",  # Caminho base
    tags=["Characters"]           # Tag usada na documentação Swagger
)

# Criar personagem
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CharacterSchema)
async def post_character(character: CharacterSchema, db: AsyncSession = Depends(get_session)):
    new_character = CharactersModel(  # Correção aqui
        name=character.name,
        description=character.description,
        image=character.image
    )

    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character

# Listar personagens
@router.get("/", response_model=List[CharacterSchema])
async def get_characters(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel))  # Correção aqui
    characters = result.scalars().all()
    return characters

# Buscar personagem por ID
@router.get("/{character_id}", response_model=CharacterSchema)
async def get_character(character_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))  # Correção aqui
    character = result.scalars().first()

    if character:
        return character
    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

# Atualizar personagem por ID
@router.put("/{character_id}", response_model=CharacterSchema)
async def put_character(character_id: int, character: CharacterSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))  # Correção aqui
    character_up = result.scalars().first()

    if character_up:
        character_up.name = character.name
        character_up.description = character.description
        character_up.image = character.image

        await db.commit()
        await db.refresh(character_up)
        return character_up

    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

# Deletar personagem
@router.delete("/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_character(character_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))  # Correção aqui
    character_del = result.scalars().first()

    if character_del:
        await db.delete(character_del)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)
