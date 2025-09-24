from model.user_model import User
from api.database import db

def get_all_users_controller():
    users = User.query.all()
    
    return users
