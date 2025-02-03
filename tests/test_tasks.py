import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Ensure the parent directory (where tasks.py is) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import tasks

class TestTaskFunctions(unittest.TestCase):

    @patch("builtins.input", return_value="Buy milk")
    def test_add_valid_task(self, mock_input):
        """Test adding a valid task"""
        task_list = []
        tasks.add_task(task_list)
        self.assertIn("Buy milk", task_list)  # Task should be in the list
        self.assertEqual(len(task_list), 1)  # Only one task should be added

    @patch("builtins.input", return_value="  ")  # Simulate empty/whitespace input
    def test_add_empty_task(self, mock_input):
        """Test that empty input does not add a task"""
        task_list = []
        tasks.add_task(task_list)
        self.assertEqual(len(task_list), 0)  # List should still be empty

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_tasks_with_tasks(self, mock_stdout):
        """Test viewing tasks when the list has tasks"""
        task_list = ["Buy milk", "Read book"]
        tasks.view_tasks(task_list)
        output = mock_stdout.getvalue()
        self.assertIn("1. Buy milk", output)
        self.assertIn("2. Read book", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_view_tasks_no_tasks(self, mock_stdout):
        """Test viewing tasks when the list is empty"""
        task_list = []
        tasks.view_tasks(task_list)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "no tasks")  # Should print "no tasks"

    @patch("builtins.input", return_value="1")
    @patch("sys.stdout", new_callable=StringIO)
    def test_complete_task_valid(self, mock_stdout, mock_input):
        """Test marking a valid task as complete"""
        task_list = ["Buy milk", "Read book"]
        tasks.complete_task(task_list)
        output = mock_stdout.getvalue()
        self.assertEqual(len(task_list), 1)  # Task list should have one item left
        self.assertNotIn("Buy milk", task_list)  # "Buy milk" should be removed
        self.assertIn("completed: Buy milk", output)  # Should confirm task completion

    @patch("builtins.input", return_value="3")
    @patch("sys.stdout", new_callable=StringIO)
    def test_complete_task_invalid_number(self, mock_stdout, mock_input):
        """Test marking a task complete with an out-of-range number"""
        task_list = ["Buy milk", "Read book"]
        tasks.complete_task(task_list)
        output = mock_stdout.getvalue()
        self.assertEqual(len(task_list), 2)  # List should remain unchanged
        self.assertIn("invalid task number", output)  # Should print error message

    @patch("builtins.input", return_value="abc")
    @patch("sys.stdout", new_callable=StringIO)
    def test_complete_task_invalid_input(self, mock_stdout, mock_input):
        """Test marking a task complete with a non-numeric input"""
        task_list = ["Buy milk", "Read book"]
        tasks.complete_task(task_list)
        output = mock_stdout.getvalue()
        self.assertEqual(len(task_list), 2)  # List should remain unchanged
        self.assertIn("invalid input", output)  # Should print error message

    @patch("sys.stdout", new_callable=StringIO)
    def test_complete_task_no_tasks(self, mock_stdout):
        """Test completing a task when there are no tasks"""
        task_list = []
        tasks.complete_task(task_list)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "no tasks to complete")  # Should print "no tasks to complete"

if __name__ == "__main__":
    unittest.main()