import asyncio
import asyncmy
from core.configs import settings

async def wait_for_db():
    tries = 0
    while tries < 10:
        try:
            conn = await asyncmy.connect(
                host=settings.DB_HOST,
                port=int(settings.DB_PORT),
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                db=settings.DB_NAME,
            )
            await conn.ensure_closed()
            print("✅ Banco de dados disponível.")
            return
        except Exception as e:
            tries += 1
            print(f"⏳ Tentativa {tries}: aguardando DB... ({e})")
            await asyncio.sleep(2)
