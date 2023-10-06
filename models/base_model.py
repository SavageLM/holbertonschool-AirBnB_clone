#!/usr/bin/python3
"""The base model for the AirBnB clone"""
from datetime import datetime
import uuid
from models import storage

class BaseModel(object):
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """__init__ Method for Base Model Class"""
        if kwargs is True:
            for name, value in kwargs.items():
                if name is not '__class__':
                    if name is not 'created_at' or name is not 'updated_at':
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value)
        else:
            self.id = str(uuid.uuid4())
            """create a new UUID and convert it to a string.
            id will contain the UUID as a string."""
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """save method of BaseModel updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """creates dict with all keys/values of __dict__ instance.
        Returns: dictionary of instance key-value pairs """
        base_dict = dict(self.__dict__)
        base_dict['__class__'] = type(self).__name__
        base_dict['created_at'] = base_dict['created_at'].isoformat()
        base_dict['updated_at'] = base_dict['updated_at'].isoformat()
        return base_dict