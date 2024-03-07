#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up the test case."""
        self.state = State()

    def tearDown(self):
        """Tear down the test case."""
        del self.state

    def test_instance(self):
        """Test if the state instance is an instance of State."""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """Test if state has the correct attributes."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
