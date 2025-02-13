import tkinter as tk
from storage import load_tasks, save_tasks

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("todo list")
        self.tasks = load_tasks()

        # headline
        self.headline = tk.Label(root, text="todo list", font=("Arial", 16, "bold"))
        self.headline.pack(pady=(10, 5))

        # task list frame
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        # task entry field
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # buttons
        self.add_button = tk.Button(root, text="add task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_task_list()

    def update_task_list(self):
        """Refresh the task frame to display current tasks."""
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(fill='x', pady=2)

            check_button = tk.Checkbutton(task_frame, command=lambda i=index: self.complete_task(i))
            check_button.pack(side='left')

            task_label = tk.Label(task_frame, text=task, anchor='w')
            task_label.pack(side='left', fill='x', expand=True)

    def add_task(self):
        """Add a new task."""
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)
            self.update_task_list()
            self.entry.delete(0, tk.END)

    def complete_task(self, index):
        """Mark a task as completed (removes from list)."""
        del self.tasks[index]
        save_tasks(self.tasks)
        self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()