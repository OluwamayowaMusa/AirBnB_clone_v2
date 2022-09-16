#!/usr/bin/python3
"""This module defines a class user"""
from curses import echo
from models.base_model import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root:Christlike1_@localhost:3306/hbnb_dev_db', echo=False)
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


Base.metadata.create_all(engine)