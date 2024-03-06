#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console."""

    def setUp(self):
        """Set up the test case."""
        self.stdout = StringIO()
        self.stderr = StringIO()
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test case."""
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def test_create(self):
        """Test the create command."""
        self.console.onecmd("create User")
        user_id = self.stdout.getvalue().strip()
        self.assertRegex(user_id, r"^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$")

    def test_show(self):
        """Test the show command."""
        self.console.onecmd("create User")
        user_id = self.stdout.getvalue().strip()
        self.stdout = StringIO()
        sys.stdout = self.stdout
        self.console.onecmd(f"show User {user_id}")
        self.assertIn(user_id, self.stdout.getvalue().strip())

    def test_destroy(self):
        """Test the destroy command."""
        self.console.onecmd("create User")
        user_id = self.stdout.getvalue().strip()
        self.console.onecmd(f"destroy User {user_id}")
        self.stdout = StringIO()
        sys.stdout = self.stdout
        self.console.onecmd(f"show User {user_id}")
        self.assertIn("no instance found", self.stdout.getvalue().strip())

    def test_all(self):
        """Test the all command."""
        self.console.onecmd("create User")
        self.console.onecmd("all User")
        output = self.stdout.getvalue().strip()
        self.assertIn("[User]", output)

    def test_update(self):
        """Test the update command."""
        self.console.onecmd("create User")
        user_id = self.stdout.getvalue().strip()
        self.console.onecmd(f"update User {user_id} name 'Holo'")
        self.stdout = StringIO()
        sys.stdout = self.stdout
        self.console.onecmd(f"show User {user_id}")
        self.assertIn("'name': 'Holo'", self.stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
