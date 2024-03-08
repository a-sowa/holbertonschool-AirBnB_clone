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

    def test_all(self):
        """Test the all method."""
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

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

    def test_reload_nonexistent_file(self):
        """Test reload method with a nonexistent file."""
        # Remove the file if it exists
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Try reloading from a nonexistent file
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertEqual(all_objects, {})

if __name__ == '__main__':
    unittest.main()
