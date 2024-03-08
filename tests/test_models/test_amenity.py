#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel and has default values."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """Test setting and getting attributes of Amenity."""
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_default_values(self):
        """Test that Amenity instances have correct default values."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_edge_cases(self):
        """Test behavior in edge cases."""
        # Example: Test if Amenity handles None gracefully
        amenity = Amenity(name=None)
        self.assertEqual(amenity.name, None)

if __name__ == '__main__':
    unittest.main()
