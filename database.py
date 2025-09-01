from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Base import Base

engine = create_engine("sqlite:///reservations.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
