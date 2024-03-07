#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up the test case."""
        self.city = City()

    def tearDown(self):
        """Tear down the test case."""
        del self.city

    def test_instance(self):
        """Test if the city instance is an instance of City."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test if city has the correct attributes."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
