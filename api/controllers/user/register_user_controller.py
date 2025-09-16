from model.user_model import User

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_user_controller(data):
    new_user = User(
        username=data['user'],
        password=data['passoword']
    )

db.session.add(new_user)
db.session.commit()
