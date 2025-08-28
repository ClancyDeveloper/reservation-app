from sqlalchemy.orm import DeclarativeBase
from datetime import timezone, datetime


class DataBase(DeclarativeBase):
    pass

class Client(DataBase):
    __tablename__ = "client"

    id = DataBase.Column(DataBase.Integer, primary_key=True, autoincrement=True)
    name = DataBase.Column(DataBase.String(120), nullable=False)
    cpf = DataBase.Column(DataBase.String(11), unique=True, nullable=False)
    email = DataBase.Column(DataBase.String(120), unique=True, nullable=False)
    phone = DataBase.Column(DataBase.String(50), unique=True, nullable=False)
    created_at = DataBase.Column(DataBase.DateTime, default=datetime.now(timezone.utc), nullable=False)
    deleted_at = DataBase.Column(DataBase.DateTime, nullable=True)

    user_id = DataBase.Column(DataBase.Integer, DataBase.ForeingKey('user.id'), nullable=False)