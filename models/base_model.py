#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

STO_TYP = getenv("HBNB_TYPE_STORAGE")
if STO_TYP == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if "created_at" not in kwargs.keys():
                self.updated_at = self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            # YAY 2 datetimes
        if STO_TYP != 'db':
            kwargs.pop('__class__', None)
        for attr, val in kwargs.items():
            setattr(self, attr, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary = dict(self.__dict__)
        dictionary.update({"__class__": type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """ Deletes the current instance from the storage """
        from models import storage
        storage.delete(self)
