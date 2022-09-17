#!/usr/bin/python3
""" The Database Storage Engine

"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place


class DBStorage:
    """ A Class that handles the database storage engine

    Attributes:
        __engine (obj): Connects to a database
        __session (obj): Queries a database
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes an instance of the class """
        dialect = 'mysql'
        driver = 'mysqldb'
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        test_dev = os.getenv('HBNB_ENV')  # Running Env
        DBStorage.__engine = \
            create_engine(f'{dialect}+{driver}://{user}:{passwd}@{host}/{db}',
                          pool_pre_ping=True)

    def all(self, cls=None):
        """ Query the database for the class cls

        Args:
            cls (class): Class to passed to query
        """
        if cls:
            obj_dict = {}
            for obj in DBStorage.__session.query(cls):
                key = cls.__name__ + '.' + obj.id
                if '_sa_instance_state' in obj.__dict__:
                    del obj.__dict__['_sa_instance_state']
                obj_dict[key] = obj
            return obj_dict
        else:
            classes = [State, City, User, Place]
            obj_dict = {}
            for clss in classes:
                for obj in DBStorage.__session.query(clss):
                    key = clss.__name__ + '.' + obj.id
                    if '_sa_instance_state' in obj.__dict__:
                        del obj.__dict__['_sa_instance_state']
                    obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """ Add new obj to current session

        Args:
            obj (object): Instance of State, City etc
        """
        DBStorage.__session.add(obj)

    def save(self):
        """ Commit all the changes in the database """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ Delete from current session

        Args:
            obj (object): Instance of State, City etc
        """
        if cls:
            DBStorage.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database and session """
        Base.metadata.create_all(DBStorage.__engine)
        session_factory = sessionmaker(bind=DBStorage.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        DBStorage.__session = Session()
