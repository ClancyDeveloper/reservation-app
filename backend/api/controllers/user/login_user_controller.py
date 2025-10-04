from flask import jsonify
from model.user_model import User
from api.database import db

def login_user_controller(data):
    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return "Usuário não encontrado"

    if not user.password == data['password']:
        return "Senha incorreta"

    return None
