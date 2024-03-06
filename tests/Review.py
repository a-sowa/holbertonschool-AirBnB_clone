#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up the test case."""
        self.review = Review()

    def tearDown(self):
        """Tear down the test case."""
        del self.review

    def test_instance(self):
        """Test if the review instance is an instance of Review."""
        self.assertIsInstance(self.review, Review)

    def test_inheritance(self):
        """Test if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """Test if review has the correct attributes."""
        attrs = {
            'place_id': '',
            'user_id': '',
            'text': ''
        }
        for attr, val in attrs.items():
            self.assertTrue(hasattr(self.review, attr))
            self.assertEqual(getattr(self.review, attr), val)

    def test_save(self):
        """Test if the save method works correctly for Review."""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict(self):
        """Test if to_dict method works correctly for Review."""
        self.review_dict = self.review.to_dict()
        self.assertEqual(self.review_dict['__class__'], 'Review')
        self.assertIsInstance(self.review_dict['created_at'], str)
        self.assertIsInstance(self.review_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
