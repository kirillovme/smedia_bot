from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):  # type: ignore
    """Модель пользователя."""
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True, index=True)
