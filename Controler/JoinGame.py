import datetime

from Models.Game import Game
from Models.User import User
import uuid
from base import Session, Base, engine
from random import randint


def join_chess_game(gid: int, uid: uuid.UUID):
    Base.metadata.create_all(engine)
    session = Session()
    game = session.query(Game).where(Game.id == gid).first()
    color=""
    if game is not None:
        if game.white_player is None and game.black_player is None:
            p = randint(4, 22) % 2
            if p == 0:
                session.query(Game).filter(Game.id == gid).update({"white_player": uid})
                color = "w"
                session.commit()
                session.close()
            else:
                session.query(Game).filter(Game.id == gid).update({"black_player": uid})
                color = "b"
                session.commit()
                session.close()
        #Podczas dołączenia drugiego gracza, gra przechodzi w stan aktywny
        else:
            if game.white_player is None and game.black_player != uid:
                session.query(Game).filter(Game.id == gid).update({"white_player": uid, "game_state": "playing", "white_last_move": datetime.datetime.now()})
                color = "w"
                session.commit()
                session.close()
            elif game.black_player is None and game.white_player != uid:
                session.query(Game).filter(Game.id == gid).update({"black_player": uid, "game_state": "playing", "black_last_move": datetime.datetime.now()})
                color = "b"
                session.commit()
                session.close()
            else:
                return -1, "none"
        return gid, color
    session.close()
    return -1, "none"

