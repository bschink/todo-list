import unittest
from unittest.mock import mock_open, patch
import sys
import os
import json

# Ensure the parent directory (where storage.py is) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import storage

class TestStorageFunctions(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    def test_load_tasks_no_file(self, mock_exists):
        """Test loading tasks when the file does not exist"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, [])

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(["Buy milk", "Read book"]))
    def test_load_tasks_with_tasks(self, mock_open, mock_exists):
        """Test loading tasks from a JSON file"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, ["Buy milk", "Read book"])

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", side_effect=json.JSONDecodeError("Expecting value", "doc", 0))
    @patch("sys.stdout", new_callable=lambda: open(os.devnull, "w"))  # Suppress print output
    def test_load_tasks_corrupted_file(self, mock_stdout, mock_open, mock_exists):
        """Test handling a corrupted JSON file (JSONDecodeError)"""
        tasks = storage.load_tasks()
        self.assertEqual(tasks, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_open):
        """Test saving tasks to a JSON file"""
        tasks = ["Buy milk", "Read book"]
        storage.save_tasks(tasks)

        mock_open.assert_called_once_with(storage.TODO_FILE, "w")
        handle = mock_open()

        # capture all write calls
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)

        # compare full output
        expected_json = json.dumps(tasks, indent=4)
        self.assertEqual(written_data, expected_json)

if __name__ == "__main__":
    unittest.main()