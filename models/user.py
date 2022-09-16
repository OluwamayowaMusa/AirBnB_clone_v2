#!/usr/bin/python3
"""This module defines a class user"""
from curses import echo
from models.base_model import BaseModel
# from models.place import Place
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from models.place import Place

engine = create_engine('mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost:3306\
                       /hbnb_dev_db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")


Base.metadata.create_all(engine)
