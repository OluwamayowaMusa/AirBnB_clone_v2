#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
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
        cond = os.getenv('HBNB_TYPE_STORAGE')
        if cond == 'db':
            return State.cities
        else:
            cities_in_state = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)

            return cities_in_state
