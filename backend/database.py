from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Base import Base

from model.user_model import User
from model.client_model import Client
from model.reservation_model import Reservation

engine = create_engine("sqlite:///reservations.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
