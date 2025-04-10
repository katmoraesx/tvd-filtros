from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.players_models import PlayersModel
from schemas.players_schemas import PlayersSchema
from core.deps import get_session


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlayersSchema)
async def post_players(player: PlayersSchema, db: AsyncSession = Depends(get_session)):
    new_player = PlayersModel(
        name = player.name,
        age = player.age,
        height = player.height,
        position = player.position,
        time = player.time,
        country = player.country,
        image = player.image
        )
    
    db.add(new_player)
    await db.commit()

    return new_player


@router.get("/", response_model=List[PlayersSchema])
async def get_players(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(PlayersModel)
        result = await session.execute(query)
        players: List[PlayersModel] = result.scalars().all()

        return players


@router.get("/{player_id}", response_model=PlayersSchema)
async def get_player(player_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query =  select(PlayersModel).filter(PlayersModel.id == player_id)
        result = await session.execute(query)
        player = result.scalars_one_or_none()

        if player:
            return player
        else:
            raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{player_id}", response_model=PlayersSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_player(player_id: int, player = PlayersSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query =  select(PlayersModel).filter(PlayersModel.id == player_id)
        result = await session.execute(query)
        player_up = result.scalars_one_or_none()
        
        if player_up:
            player_up.name = player.name
            player_up.age = player.age
            player_up.height = player.height
            player_up.position = player.position
            player_up.time = player.time
            player_up.country = player.country
            player_up.image = player.image

            await session.commit()
            return player_up
        else:
            raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{players_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(player_id: int, db: AsyncSession= Depends(get_session)):
    async with db as session:
        query =  select(PlayersModel).filter(PlayersModel.id == player_id)
        result = await session.execute(query)
        player_del = result.scalars_one_or_none()

        if player_del:
            await session.delete(player_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)