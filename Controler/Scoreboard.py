from base import Session
from Models.User import User
from sqlalchemy import desc
from flask import jsonify

def scoreboard():
    session = Session()
    users = session.query(User.nick, User.mmr).order_by(desc(User.mmr))

    if users is not None:
        users = [(r.nick, r.mmr) for r in users]
        session.close()
        return jsonify(list=users[:10])

    session.close()
    return jsonify(users=[])

