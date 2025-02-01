def add_task(tasks):
    """add a task to the todo list"""
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print("task added!")

def view_tasks(tasks):
    """view the tasks in the todo list"""
    if tasks:
        print("tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("no tasks")

def complete_task(tasks):
    """mark a task as complete"""
    if tasks:
        view_tasks(tasks)
        task_number = input("enter the number of the task to mark as complete: ").strip()
        if task_number.isdigit():
            task_number = int(task_number)
            if 1 <= task_number <= len(tasks):
                task = tasks.pop(task_number - 1)
                print(f"completed: {task}")
            else:
                print("invalid task number")
        else:
            print("invalid input")
    else:
        print("no tasks to complete")

def main():
    """main loop for the todo list cli"""
    tasks = []

    while True:
        print("\nwhat would you like to do?")
        print("1. view tasks")
        print("2. add a task")
        print("3. mark a task as complete")
        print("4. exit")
        choice = input("enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice. please try again")

if __name__ == "__main__":
    main()