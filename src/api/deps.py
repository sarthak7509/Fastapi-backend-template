from src.db.session import session as sessionlocal

async def get_db():
    async with sessionlocal() as session:
        yield session