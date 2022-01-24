from base import Session
from Models.Game import Game
from flask import jsonify


def get_game_data(gid, uid):
    session = Session()
    game = session.query(Game).filter(Game.id == gid).first()
    if game is not None:
        if uid == str(game.white_player) or uid == str(game.black_player):
            return jsonify(game_id=gid, fen=game.FEN, game_status=game.game_state)
    return jsonify(fen='')







