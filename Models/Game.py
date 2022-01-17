from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from base import Base


class Game(Base):
    __tablename__ = "game"
    id = Column(UUID, primary_key=True)
    white_player = Column(UUID, ForeignKey('user.id'))
    black_player = Column(UUID, ForeignKey('user.id'))
    white_player_time_left = Column(INTEGER)
    black_player_time_left = Column(INTEGER)
    FEN = Column(String)
    player_to_play = Column(String)
    game_state = Column(String)

