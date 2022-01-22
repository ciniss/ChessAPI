from base import Session, engine, Base
from Models.User import User
from uuid import uuid4
import hashlib


def addUser(name: str, email: str, password: str):
    Base.metadata.create_all(engine)
    u_id = uuid4()
    user = User(u_id, name, email, hashlib.md5(password.encode()).hexdigest(), 2500)
    session = Session()
    session.add(user)
    session.commit()
    session.close()
    return u_id
