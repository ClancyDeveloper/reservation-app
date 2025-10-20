from model.user_model import User

def validate_login_user(data):
    user = User.query.filter_by(username=data["username"]).first()

    if not user:
        return "User not found"

    if not user.password == data["password"]:
        return "Incorrect password"

    return None
