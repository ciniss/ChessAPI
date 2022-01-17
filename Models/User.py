from sqlalchemy import Column, INTEGER, String
from sqlalchemy.dialects.postgresql import UUID
from base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True)
    nick = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    elo = Column(INTEGER)