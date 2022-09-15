#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from mysqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from mysqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://root:Christlike1_@localhost:3306\
                       /airbnb',
                       echo=False)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    name = Column(String(256))


Base.metadata.create_all(engine)
