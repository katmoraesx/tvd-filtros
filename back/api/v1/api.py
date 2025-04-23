from fastapi import APIRouter
from api.v1.endpoints import characters

api_router = APIRouter()

api_router.include_router(characters.router, prefix="/characters", tags=["Characters"])
