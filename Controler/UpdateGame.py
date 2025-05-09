import datetime

from base import Session, engine
from Models.Game import Game
from Models.User import User
import chess
from flask import jsonify
import uuid
def update_game(gid, uid, move, time):
    session = Session()
    game = session.query(Game).filter(Game.id == gid).first()
    if game is None:
        return jsonify(status="err_no_game", fen="")
    if uid != str(game.white_player) and uid != str(game.black_player):
        return jsonify(status="err_player_auth", fen="")
    if game.game_state != "playing":
        return jsonify(status="game_finished", fen="")
    prev_FEN = game.FEN
    board = chess.Board(prev_FEN)
    player = 'n'
    #Getting player from fen
    for i in range(len(prev_FEN)):
        if prev_FEN[i] == ' ':
            player = prev_FEN[i+1]
            break
    if (uid == str(game.white_player) and player == 'w') or (uid == str(game.black_player) and player == 'b'):
        if chess.Move.from_uci(move) in board.legal_moves:
            move = chess.Move.from_uci(move)
            board.push(move)

            if player == "w":
                if (datetime.datetime.now() - game.black_last_move).seconds > 30:
                    session.query(Game).filter(Game.id == gid).update({Game.game_state: "black_win"})
                    return jsonify(fen=game.FEN, status="good", game_status="black_win")
            else:
                if (datetime.datetime.now() - game.white_last_move).seconds > 30:
                    session.query(Game).filter(Game.id == gid).update({Game.game_state: "white_win"})
                    return jsonify(fen=game.FEN, status="good", game_status="white_win")
            if player == 'w':
                session.query(Game).filter(Game.id == gid).update({
                    "white_last_move":  datetime.datetime.now(),
                    "player_to_play": "b"})
            else:
                session.query(Game).filter(Game.id == gid).update({
                    "black_last_move": datetime.datetime.now(),
                    "player_to_play": "w"})
            res_fen = board.fen()
            is_checkmate = board.is_checkmate()
            is_stealmate = board.is_stalemate()
            game_status = ""
            if is_checkmate and player == "w":
                game_status += "white_win"
                session.query(User).filter(User.id == game.black_player).update({User.mmr: User.mmr - 15})
                session.query(User).filter(User.id == game.white_player).update({User.mmr: User.mmr + 15})
            elif is_checkmate and player == "b":
                game_status += "black_win"
                session.query(User).filter(User.id == game.black_player).update({User.mmr: User.mmr + 15})
                session.query(User).filter(User.id == game.white_player).update({User.mmr: User.mmr - 15})
            elif is_stealmate:
                game_status += "draw"
            else:
                game_status += "playing"
            session.query(Game).filter(Game.id == gid).update({'FEN': board.fen(), 'game_state': game_status})
            session.commit()
            session.close()
            return jsonify(fen=res_fen, status="good", game_status=game_status, opponent_time_left=datetime.datetime.now())
        return jsonify(status="err_bad_move", fen="")
    return jsonify(status="err_wrong_player", fen="")



