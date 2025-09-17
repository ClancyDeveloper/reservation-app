from model.user_model import User
from api.database import db

def register_user_controller(data):
    new_user = User(
        username=data['username'],
        password=data['password']
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user
