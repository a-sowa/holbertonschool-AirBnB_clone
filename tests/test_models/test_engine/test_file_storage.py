#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        FileStorage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.file_storage.new(obj)
        all_objects = self.file_storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, all_objects)

    def test_save_reload(self):
        """Test the save and reload methods."""
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.save()

        # Create a new FileStorage instance to reload
        new_file_storage = FileStorage()
        new_file_storage.reload()

        all_objects = new_file_storage.all()

        key1 = f"{obj1.__class__.__name__}.{obj1.id}"
        key2 = f"{obj2.__class__.__name__}.{obj2.id}"

        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)

if __name__ == '__main__':
    unittest.main()
