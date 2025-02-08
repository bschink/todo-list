import os
import json

TODO_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file (if it exists) and returns a list."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"⚠ Warning: Could not read tasks file ({e}). Starting fresh.")
        return []

def save_tasks(tasks):
    """Saves tasks to a JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)