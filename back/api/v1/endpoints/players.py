from typing import List, Optional
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.players_models import PlayersModel
from models.players_models import TeamsModel
from schemas.players_schemas import PlayersSchema, PlayersTeamsSchema
from schemas.teams_schemas import TeamsSchema
from core.deps import get_session

router = APIRouter()

# CRUD para Times (Teams)

@router.post("/teams/", status_code=status.HTTP_201_CREATED, response_model=TeamsSchema)
async def post_team(team: TeamsSchema, db: AsyncSession = Depends(get_session)):
    new_team = TeamsModel(
        name=team.name,
        city=team.city,
        arena=team.arena,
        image_arena=team.image_arena
    )

    db.add(new_team)
    await db.commit()
    await db.refresh(new_team)
    return new_team


@router.get("/teams/", response_model=List[TeamsSchema])
async def get_teams(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(TeamsModel))
    teams: List[TeamsModel] = result.scalars().all()
    return teams


@router.get("/teams/{team_id}", response_model=TeamsSchema)
async def get_team(team_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(TeamsModel).filter(TeamsModel.id == team_id))
    team = result.scalars().first()

    if team:
        return team
    raise HTTPException(detail="Team not found", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/teams/{team_id}", response_model=TeamsSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_team(team_id: int, team: TeamsSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(TeamsModel).filter(TeamsModel.id == team_id))
    team_up = result.scalars().first()

    if team_up:
        team_up.name = team.name
        team_up.city = team.city
        team_up.arena = team.arena
        team_up.image_arena = team.image_arena

        await db.commit()
        await db.refresh(team_up)
        return team_up

    raise HTTPException(detail="Team not found", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/teams/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_team(team_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(TeamsModel).filter(TeamsModel.id == team_id))
    team_del = result.scalars().first()

    if team_del:
        await db.delete(team_del)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(detail="Team not found", status_code=status.HTTP_404_NOT_FOUND)

# CRUD para Jogadores (Players)

@router.post("/players/", status_code=status.HTTP_201_CREATED, response_model=PlayersSchema)
async def post_player(player: PlayersSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(TeamsModel).filter(TeamsModel.id == player.team_id))
    team = result.scalars().first()

    if not team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")

    new_player = PlayersModel(
        name=player.name,
        age=player.age,
        height=player.height,
        position=player.position,
        country=player.country,
        image=player.image,
        team_id=player.team_id  
    )

    db.add(new_player)
    await db.commit()
    await db.refresh(new_player)
    return new_player


@router.get("/players/", response_model=List[PlayersSchema])
async def get_players(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(PlayersModel))
    players: List[PlayersModel] = result.scalars().all()
    return players


@router.get("/players/{player_id}", response_model=PlayersTeamsSchema)
async def get_player(player_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(PlayersModel).filter(PlayersModel.id == player_id))
    player = result.scalars().first()

    if player:
        return player
    raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/players/{player_id}", response_model=PlayersSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_player(player_id: int, player: PlayersSchema, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(PlayersModel).filter(PlayersModel.id == player_id))
    player_up = result.scalars().first()

    if player_up:
        player_up.name = player.name
        player_up.age = player.age
        player_up.height = player.height
        player_up.position = player.position
        player_up.country = player.country
        player_up.image = player.image
        player_up.team_id = player.team_id  

        await db.commit()
        await db.refresh(player_up)
        return player_up

    raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/players/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_player(player_id: int, db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(PlayersModel).filter(PlayersModel.id == player_id))
    player_del = result.scalars().first()

    if player_del:
        await db.delete(player_del)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(detail="Player not found", status_code=status.HTTP_404_NOT_FOUND)
