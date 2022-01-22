from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from base import Base

import chess
import uuid
class Game(Base):
    __tablename__ = "games"
    id = Column(INTEGER, primary_key=True)
    white_player = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    black_player = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    white_player_time_left = Column(INTEGER)
    black_player_time_left = Column(INTEGER)
    FEN = Column(String)
    player_to_play = Column(String)
    game_state = Column(String)

    def __init__(self, game_id):
        self.id = game_id
        self.white_player = None
        self.black_player = None
        self.white_player_time_left = 600
        self.black_player_time_left = 600
        self.FEN = chess.STARTING_FEN
        self.player_to_play = "w"
        self.game_state = "play"