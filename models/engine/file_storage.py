#!/usr/bin/python3
"""Module for File Storage class.

This module provides the FileStorage class which handles serialization and
deserialization of all class instances to and from a JSON file.
"""

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj
                    in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "Review": Review,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
            for obj_id, obj in objs.items():
                cls_name = obj['__class__']
                if cls_name in class_dict:
                    cls = class_dict[cls_name]
                    self.__objects[obj_id] = cls(**obj)
        except FileNotFoundError:
            pass
