from config.config import DATABASE_URL
from models.models import Base, User
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> AsyncEngine:
    """Инициализация базы данных на основе моделей."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return engine


async def get_or_create_user(session: AsyncSession, telegram_id: int) -> bool:
    """Создание или получение пользователя из базы данных."""
    result = await session.get(User, telegram_id)
    if not result:
        new_user = User(telegram_id=telegram_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return False
    return True
