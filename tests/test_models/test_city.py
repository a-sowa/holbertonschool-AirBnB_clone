#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Class to test City."""

    def setUp(self):
        """set up for the test case."""
        self.city = City()

    def tearnDown(self):
        """Clean up after the test case."""
        del self.city
    
    def test_instance(self):
        """Test for proper initialization of City instance."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertIsInstance(self.city, BaseModel)
    
    def test_attributes(self):
        """Test if City
          has the correct attributes."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.id, "")


if __name__ == '__main__':
    unittest.main()
