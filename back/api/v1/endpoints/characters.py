from typing import List, Optional
from fastapi import APIRouter, status, Depends, HTTPException, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.characters_models import CharactersModel
from models.groups_models import GroupsModel
from schemas.characters_schemas import CharacterSchema, CharacterCreateSchema
from core.deps import get_session

router = APIRouter()

# Criar personagem com grupos
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CharacterSchema)
async def post_character(character: CharacterCreateSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(GroupsModel).filter(GroupsModel.name.in_(character.groups)))
    groups = result.scalars().all()

    if not groups and character.groups:
        raise HTTPException(status_code=400, detail="Grupos não encontrados")

    new_character = CharactersModel(
        name=character.name,
        age=character.age,
        height=character.height,
        role=character.role,
        origin=character.origin,
        description=character.description,
        image=character.image,
        groups=groups
    )

    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character

# Listar personagens com filtro por grupo
@router.get("/", response_model=List[CharacterSchema])
async def get_characters(grupo: Optional[str] = Query(None), db: AsyncSession = Depends(get_session)):
    query = select(CharactersModel)

    if grupo:
        query = query.join(CharactersModel.groups).filter(GroupsModel.name == grupo)

    result = await db.execute(query)
    characters = result.scalars().unique().all()
    return characters

# Buscar personagem por ID
@router.get("/{character_id}", response_model=CharacterSchema)
async def get_character(character_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))
    character = result.scalars().first()

    if character:
        return character
    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

# Atualizar personagem por ID (com grupos)
@router.put("/{character_id}", response_model=CharacterSchema)
async def put_character(character_id: int, character: CharacterCreateSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))
    character_up = result.scalars().first()

    if character_up:
        character_up.name = character.name
        character_up.age = character.age
        character_up.height = character.height
        character_up.role = character.role
        character_up.origin = character.origin
        character_up.description = character.description
        character_up.image = character.image

        result_groups = await db.execute(select(GroupsModel).filter(GroupsModel.name.in_(character.groups)))
        character_up.groups = result_groups.scalars().all()

        await db.commit()
        await db.refresh(character_up)
        return character_up

    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

# Deletar personagem
@router.delete("/{character_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_character(character_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(CharactersModel).filter(CharactersModel.id == character_id))
    character_del = result.scalars().first()

    if character_del:
        await db.delete(character_del)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)
