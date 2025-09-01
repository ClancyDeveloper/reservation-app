from model.user_model import User
from database import SessionLocal

def list_users():
    session = SessionLocal
    users = session.query(User).all()
    session.close()
    return users
