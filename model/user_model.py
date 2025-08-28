from sqlalchemy.orm import DeclarativeBase

class DataBase(DeclarativeBase):
    pass

class User(DataBase):
    __tablename__ = "user"

    id = DataBase.Column(DataBase.Integer, primary_key=True, autoincrement=True)
    username = DataBase.Column(DataBase.String(120), nullable=False)
    password = DataBase.Column(DataBase.Integer(50), nullable=False)
    

