from model.user_model import User

def valid_username(data):
    username = data.get('username')
    duplicate_user = User.query.filter_by(username=username).first()
    if duplicate_user:
        return "Username already exists"
        
    return None