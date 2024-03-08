#!/usr/bin/python3
import sys
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBaseModel(unittest.TestCase):
    """Classe to test the BaseModel."""

    def test_instance_creation(self):
        """Test the creation of an instance and the presence of attributs."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_to_dict(self):
        """Test the method to_dict."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My_First_Model")
        self.assertEqual(model_dict['my_number'], 89)

    def test_init_from_dict(self):
        """Test the initialisation of BaseModel with **kwargs."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        my_new_model = BaseModel(**model_dict)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)

    def test_str(self):
        instance = BaseModel()
        str_representation = str(instance)
        self.assertTrue('[BaseModel]' in str_representation)
        self.assertTrue('({})'.format(instance.id) in str_representation)

    def test_save(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

if __name__ == '__main__':
    unittest.main()
