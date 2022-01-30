from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

from Controler.CreateGame import create_game
from Controler.CreateUser import addUser
from Controler.JoinGame import join_chess_game
from Controler.UpdateGame import update_game
from Controler.GetGame import get_game_data
from Controler.Login import log_in
app = Flask(__name__)

#GET

@app.route('/scoreboard', methods=['GET'])
def get_scoreboard():  # put application's code here
    return jsonify()

@app.route("/login",methods=["GET"])
def login():
    req_data = request.get_json(force=True)
    nick = req_data['username']
    pswd = req_data['password']
    if nick is None or pswd is None:
        abort(404, "Missing data")
    return log_in(nick, pswd)
@app.route("/game", methods=['GET'])
def get_game():
    req_data = request.get_json(force=True)
    gid = request.args.get('id')
    uid = req_data['user_id']
    return get_game_data(gid, uid)

#POST
@app.route('/register', methods=['POST'])
def register():  # put application's code here
    req_data = request.get_json()
    name = req_data["username"]
    email = req_data["email"]
    password = req_data["password"]
    u_id = addUser(name, email, password)
    return jsonify(uid=u_id)

@app.route('/create_game', methods = ['POST'])
def start_game():
    g_id = create_game()
    return jsonify(game_id=str(g_id))

#PUT
@app.route('/join_game', methods=['PUT'])
def join_game():
    req_data = request.get_json()
    g_id = req_data['game_id']
    u_id = req_data['user_id']
    r_id, color = join_chess_game(g_id, u_id)

    if r_id == g_id:
        return jsonify(game_id=g_id, status='ok', color=color)
    return jsonify(status="no such aviable game")

@app.route('/game', methods=['PUT'])
def upd_game():  # put application's code here
    req_data = request.get_json()
    gid = request.args.get('id')
    uid = req_data['user_id']
    move = req_data['move']
    timeleft = req_data['time_left']
    return update_game(gid, uid, move, timeleft)


if __name__ == '__main__':
    app.run(debug=True)
