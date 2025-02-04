import unittest
from unittest.mock import mock_open, patch
import sys
import os

# Ensure the parent directory (where storage.py is) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import storage

class TestStorageFunctions(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    def test_load_tasks_no_file(self, mock_exists):
        """Test loading tasks when the file does not exist"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, [])  # Should return an empty list

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data="Buy milk\nRead book\n")
    def test_load_tasks_with_tasks(self, mock_open, mock_exists):
        """Test loading tasks from a file"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, ["Buy milk", "Read book"])  # Should return a list with tasks

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", side_effect=UnicodeDecodeError("utf-8", b"", 0, 1, "error"))
    @patch("sys.stdout", new_callable=lambda: open(os.devnull, "w"))  # Suppress print output
    def test_load_tasks_corrupted_file(self, mock_stdout, mock_open, mock_exists):
        """Test handling a corrupted file (UnicodeDecodeError)"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, [])  # Should return an empty list

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_open):
        """Test saving tasks to a file"""
        tasks = ["Buy milk", "Read book"]
        storage.save_tasks(tasks)

        mock_open.assert_called_once_with(storage.TODO_FILE, "w")  # Ensure file was opened in write mode
        handle = mock_open()
        handle.write.assert_any_call("Buy milk\n")  # Ensure correct data was written
        handle.write.assert_any_call("Read book\n")

if __name__ == "__main__":
    unittest.main()