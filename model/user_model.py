from sqlalchemy import String, Integer, Column
from .Base import Base
from api.database import db

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)
    

