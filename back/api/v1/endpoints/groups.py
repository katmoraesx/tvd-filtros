from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from core.deps import get_session
from models.groups_models import GroupsModel
from schemas.groups_schemas import GroupSchemaCreate, GroupSchemaRead, GroupSchemaUpdate

router = APIRouter()

@router.post("/", response_model=GroupSchemaRead, status_code=status.HTTP_201_CREATED)
async def create_group(group: GroupSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_group = GroupsModel(**group.dict())
    db.add(new_group)
    await db.commit()
    await db.refresh(new_group)
    return new_group

@router.get("/", response_model=List[GroupSchemaRead])
async def list_groups(db: AsyncSession = Depends(get_session)):
    result = await db.execute(
        select(GroupsModel).options(selectinload(GroupsModel.characters))
    )
    return result.scalars().all()

@router.get("/{group_id}", response_model=GroupSchemaRead)
async def get_group(group_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(
        select(GroupsModel)
        .options(selectinload(GroupsModel.characters))  # Carrega personagens relacionados
        .filter_by(id=group_id)
    )
    group = result.scalar_one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")
    return group

@router.put("/{group_id}", response_model=GroupSchemaRead)
async def update_group(group_id: int, group_data: GroupSchemaUpdate, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(GroupsModel).filter_by(id=group_id))
    group = result.scalar_one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")

    for key, value in group_data.dict(exclude_unset=True).items():
        setattr(group, key, value)

    await db.commit()
    await db.refresh(group)
    return group

@router.delete("/{group_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_group(group_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(GroupsModel).filter_by(id=group_id))
    group = result.scalar_one_or_none()
    if not group:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")

    await db.delete(group)
    await db.commit()
    return None
