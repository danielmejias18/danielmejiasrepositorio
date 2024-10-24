from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///Pygubu/Pygubu/model/db.sqlite")
engine.connect()
base = declarative_base()
session = sessionmaker(bind=engine)
