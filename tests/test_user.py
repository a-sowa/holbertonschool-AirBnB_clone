#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_user_instance(self):
        """Test if the user is an instance of User."""
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_user_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes(self):
        """Test if user has the correct attributes."""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")

    def test_user_save(self):
        """Test if the save method works correctly for User."""
        my_user = User()
        my_user.save()
        self.assertNotEqual(my_user.created_at, my_user.updated_at)

    def test_user_to_dict(self):
        """Test if to_dict method works correctly for User."""
        my_user = User()
        user_dict = my_user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
