from base import Session
from Models.Game import Game
from flask import jsonify


def get_game_data(gid, uid):
    session = Session()
    game = session.query(Game).filter(Game.id == gid).first()
    if game is not None:
        fen = game.FEN
        st = game.game_state
        if uid == str(game.white_player) or uid == str(game.black_player):
            session.close()
            return jsonify(game_id=gid, fen=fen, game_status=st)
    session.close()
    return jsonify(fen='')







