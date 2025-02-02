def add_task(task_list):
    """add a task to the todo list"""
    task = input("Enter a task: ").strip()
    if task:
        task_list.append(task)
        print("task added!")

def view_tasks(task_list):
    """view the tasks in the todo list"""
    if task_list:
        print("tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
    else:
        print("no tasks")

def complete_task(task_list):
    """mark a task as complete"""
    if task_list:
        view_tasks(task_list)
        task_number = input("enter the number of the task to mark as complete: ").strip()
        if task_number.isdigit():
            task_number = int(task_number)
            if 1 <= task_number <= len(task_list):
                task = task_list.pop(task_number - 1)
                print(f"completed: {task}")
            else:
                print("invalid task number")
        else:
            print("invalid input")
    else:
        print("no tasks to complete")