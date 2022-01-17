from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/game', methods=['GET'])
def get_game():  # put application's code here
    return jsonify(result='Hello World!')

@app.route('/game', methods=['POST'])
def post_game():  # put application's code here

    id = request.args.get('id')
    request_data = request.json

    return jsonify(id=id)

if __name__ == '__main__':
    app.run()
