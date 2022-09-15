#!/usr/bin/python3
""" Place Module for HBNB project """
from curses import echo
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:Christlike1_@localhost:3306\
                       /airbnb',
                       echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'place'

    city_id = Column(String(256))
    user_id = Column(String(256))
    name = Column(String(256))
    description = Column(String(256))
    number_rooms = Column(Integer)
    number_bathrooms = Column(Integer)
    max_guest = Column(Integer)
    price_by_night = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = Column(ARRAY)


Base.metadata.create_all(engine)
