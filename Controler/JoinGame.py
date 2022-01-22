from Models.Game import Game
from Models.User import User
import uuid
from base import Session, Base, engine


def join_chess_game(gid, uid: uuid.UUID):
    Base.metadata.create_all(engine)
    session = Session()
    game = session.query(Game).where(Game.id == gid).first()
    if game is not None:
        if game.white_player is None:
            setattr(game, 'white_player', uid)
            session.commit()
            session.close()
            return game.id
        elif game.black_player is None:
            #game.black_player = uid
            setattr(game, 'black_player', uid)
            session.commit()
            session.close()
            return game.id
    session.close()
    return -1

