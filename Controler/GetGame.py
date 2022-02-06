import datetime

from base import Session
from Models.Game import Game
from Models.User import User
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
            white_n = session.query(User).filter(User.id == game.white_player).first()
            if white_n:
                white_n = white_n.nick
            else:
                white_n = "none"
            black_n = session.query(User).filter(User.id == game.black_player).first()

            if black_n:
                black_n = black_n.nick
            else:
                black_n = "none"
            session.close()
            return jsonify(game_id=gid, fen=fen, game_status=st,
                           white_time_left=b_t_l, black_time_left=w_t_l,
                           white_nick=white_n, black_nick=black_n)
    session.close()
    return jsonify(fen='')







