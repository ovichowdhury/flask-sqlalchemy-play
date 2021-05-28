from db import db
from models.user_model import User


def create_user(data):
    u = User(**data)
    db.session.add(u)
    db.session.commit()
    return u

def get_user():
    users = User.query.all()
    users = [u.as_dict() for u in users]
    return users

def update_user(id, data):
    User.query.filter_by(id= id).update(dict(**data))
    db.session.commit()

def delete_user(id):
    u = User.query.get(id)
    db.session.delete(u)
    db.session.commit()