from sqlalchemy.orm import DeclarativeBase
from datetime import timezone, datetime

class DataBase(DeclarativeBase):
    pass

class Reservation(DataBase):
    __tablename__ = 'reservation'

    id = DataBase.Column(DataBase.Integer, primary_key=True, autoincrement=True)
    name = DataBase.Column(DataBase.String(100), nullable=False)
    reserved_at = DataBase.Column(DataBase.DateTime, nullable=False)
    expires_at = DataBase.Column(DataBase.DateTime, nullable=False)
    created_at = DataBase.Column(DataBase.DateTime, default=datetime.now(timezone.utc), nullable=False)
    description = DataBase.Column(DataBase.String(300), nullable=True)

    client_id = DataBase.Column(DataBase.Integer, DataBase.ForeingKey('client.id'), nullable=False)