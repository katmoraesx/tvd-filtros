# db_init.py
import asyncio
import time

# Aguarda 10 segundos antes de tentar conexão (ajuste se necessário)
time.sleep(20)

from criar_tabelas import create_tables
from popular_banco import popular

async def init():
    await create_tables()
    await popular()

if __name__ == "__main__":
    asyncio.run(init())
