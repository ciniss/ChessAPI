from Models.Game import Game
from base import Session, engine,Base
import chess
from random import randrange

def create_game():
    Base.metadata.create_all(engine)
    g_id = randrange(1, 2000000)
    game = Game(g_id)

    session = Session()
    session.add(game)
    session.commit()
    session.close()
    return g_id
