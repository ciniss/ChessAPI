import datetime

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
            current_time = datetime.datetime.now()
            w_t_l = (current_time-game.white_last_move).seconds
            b_t_l = (current_time-game.black_last_move).seconds
            session.close()
            return jsonify(game_id=gid, fen=fen, game_status=st, black_time_left=b_t_l, white_time_left=w_t_l)
    session.close()
    return jsonify(fen='')







