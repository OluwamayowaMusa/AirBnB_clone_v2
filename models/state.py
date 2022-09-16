#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(60), nullable=False)

    cities = relationship('City', backref=backref('state'))

    @property
    def cities(self):
        """ Gets the City with in a State """
        return State.cities
