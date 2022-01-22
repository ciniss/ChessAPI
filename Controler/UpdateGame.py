from base import Session
from Models.Game import Game
import chess
import uuid
def update_game(gid, uid, move, time):
    session = Session()
    game = session.query(Game).filter(Game.id == gid).first()
    if game is None:
        return "no_game"
    if uid != str(game.white_player) and uid != str(game.black_player):
        return "player_authorization_error"

    prev_FEN = game.FEN
    board = chess.Board(prev_FEN)
    player = 'n'
    for i in range(len(prev_FEN)):
        if prev_FEN[i] == ' ':
            player = prev_FEN[i+1]
            break
    if (uid == str(game.white_player) and player == 'w') or (uid == str(game.black_player) and player == 'b'):
        if chess.Move.from_uci(move) in board.legal_moves:
            move = chess.Move.from_uci(move)
            board.push(move)
            if player == 'w':
                session.query(Game).filter(Game.id == gid).update({"white_player_time_left": time})
            else:
                session.query(Game).filter(Game.id == gid).update({"black_player_time_left": time})
            session.query(Game).filter(Game.id == gid).update({'FEN': board.board_fen()})
            session.commit()
            session.close()
            return board.fen()
    return "bad_move"



