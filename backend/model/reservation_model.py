from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from api.database import db


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    reserved_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    description = Column(String(300), nullable=True)

    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)