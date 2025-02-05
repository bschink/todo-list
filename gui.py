import tkinter as tk
from storage import load_tasks, save_tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("todo list")

        # Load tasks from storage
        self.tasks = load_tasks()

        # Task List (Listbox)
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.update_task_list()

        # Task Entry Field
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="add task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="complete task", command=self.complete_task)
        self.complete_button.pack()

    def update_task_list(self):
        """Refresh the Listbox to display current tasks."""
        self.task_listbox.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        """Add a new task."""
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)  # Save to file
            self.update_task_list()
            self.entry.delete(0, tk.END)

    def complete_task(self):
        """Mark a selected task as completed (removes from list)."""
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            save_tasks(self.tasks)  # Save to file
            self.update_task_list()

def run_gui():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()