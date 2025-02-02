import os

TODO_FILE = "tasks.txt"

def load_tasks():
    """Loads tasks from a file (if it exists) and returns a list."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"⚠ Warning: Could not read tasks file ({e}). Starting fresh.")
        return []
    
def save_tasks(tasks):
    """Saves tasks to a file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")