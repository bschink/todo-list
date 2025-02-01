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

def main():
    """main loop for the todo list cli"""
    tasks = []

    while True:
        print("\nwhat would you like to do?")
        print("1. view tasks")
        print("2. add a task")
        print("3. exit")
        choice = input("enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("invalid choice. please try again")

if __name__ == "__main__":
    main()