from base import Session
from Models.User import User
from uuid import uuid4
import hashlib
from flask import jsonify

def log_in(user_nickname, pswd):
    session = Session()
    h_pswd = hashlib.md5(pswd.encode()).hexdigest()
    user = session.query(User).filter(User.nick == user_nickname, User.password == h_pswd).first()

    if user is not None:
        uuuid = user.id
        session.close()
        return jsonify(uid=uuuid)

    session.close()
    return jsonify(uid="-1")

