from database import SessionLocal
from model.user_model import User
from datetime import datetime, timezone

def create_user(username, password):
    session = SessionLocal()
    user = User(
        username=username,
        password=password
    )
    session.add(User)
    session.commit()
    session.refresh(user)
    session.close()
    return user
