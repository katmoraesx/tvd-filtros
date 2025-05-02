import asyncio
from criar_tabelas import create_tables
from popular_banco import popular
from wait_db import wait_for_db  # ← nova importação

async def init():
    await wait_for_db()          # ← espera o banco estar pronto
    await create_tables()
    await popular()

if __name__ == "__main__":
    asyncio.run(init())
