#!/usr/bin/python3
"""Module for Base Model.

This module provides the BaseModel class used as the base class for
all other classes in our AirBnB clone project. It handles initialization,
serialization, and deserialization of instances.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines the base model with common attributes and methods
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the base model.
        Attributes:
            id (str): The unique identifier for each instance.
            created_at (datetime): The current datetime when an
            instance is created.
            updated_at (datetime): The current datetime when an
            instance is created
                                   and to be updated every time
                                   the object changes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary containing all keys/values of the
        instance's __dict__.

        This dictionary includes the key __class__ with the name of the class.
        The datetime attributes are converted to strings in ISO format.

        Returns:
            dict: A dictionary containing all keys/values of the
            instance's __dict__.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
