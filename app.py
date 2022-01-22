from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

#GET
@app.route('/game', methods=['GET'])
def get_game():  # put application's code here
    ida = request.args.get("id")
    json = request.get_json()

    return jsonify(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1 +' + ida + " + " + json["id"])


@app.route('/scoreboard', methods=['GET'])
def get_scoreboard():  # put application's code here
    return jsonify()



#POST
@app.route('/game', methods=['PUT'])
def post_game():  # put application's code here
    return jsonify(fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')


@app.route('/register', methods=['POST'])
def register():  # put application's code here
    pass



if __name__ == '__main__':
    app.run()
