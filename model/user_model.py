from sqlalchemy import String, Integer, Column
from .Base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)
    

