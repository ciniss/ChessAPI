from sqlalchemy import Column, INTEGER, String
from sqlalchemy.dialects.postgresql import UUID
from base import Base
import uuid

class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nick = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    mmr = Column(INTEGER)

    def __init__(self, id, nick, email, password, mmr):
        self.id = id
        self.nick = nick
        self.email = email
        self.password = password
        self.mmr = mmr
