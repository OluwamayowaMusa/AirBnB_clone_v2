#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []

    reviews = relationship('Review', backref=backref('place'))

    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False,
                             backref='place_amenities')

    @property
    def reviews(self):
        """ Get the reviews """
        return Place.reviews

    @property
    def amenities(self):
        """ Get the list of amenities availiable
            Set the amenities
        """
        return Place.amenity_ids

    @amenities.setter
    def amenities(self, value):
        """ Sets the amenities """
        from models.amenity import Amenity
        if type(value) == Amenity:
            Place.amenity_ids.append(value)
