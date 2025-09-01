import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal
from model.user_model import User
from datetime import datetime, timezone

session = SessionLocal()


new_user = User(
    username = 'UsuarioTeste',
    password = 'senhadeteste@123'
)

session.add(new_user)
session.commit()

users = session.query(User).all()
for u in users:
    print(u.id, u.username, u.password)

session.close()
