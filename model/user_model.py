from sqlalchemy import String, Integer, Column
from .Base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Base.Integer, primary_key=True, autoincrement=True)

    username = Column(String(120), nullable=False)
    password = Column(Integer(50), nullable=False)
    

