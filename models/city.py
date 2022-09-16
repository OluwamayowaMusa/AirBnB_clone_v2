#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306\
                       /hbnb_dev_db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship('Place', backref="city", cascade='all, delete')


Base.metadata.create_all(engine)
