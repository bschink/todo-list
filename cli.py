import tasks
import storage

def run_cli():
    """main loop for the todo list cli"""
    task_list = storage.load_tasks()

    while True:
        print("\nwhat would you like to do?")
        print("1. view tasks")
        print("2. add a task")
        print("3. mark a task as complete")
        print("4. exit")
        choice = input("enter your choice: ").strip()

        if choice == "1":
            tasks.view_tasks(task_list)
        elif choice == "2":
            tasks.add_task(task_list)
            storage.save_tasks(task_list)
        elif choice == "3":
            tasks.complete_task(task_list)
            storage.save_tasks(task_list)
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice. please try again")