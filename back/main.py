from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

from fastapi.middleware.cors import CORSMiddleware

# IMPORTANTE: isso importa os modelos para garantir que as tabelas sejam registradas
from models import characters_models, groups_models

app = FastAPI(title="API personagens de TVD")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas dos personagens e dos grupos
app.include_router(api_router, prefix="/api/v1")

