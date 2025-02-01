# TODO add the real functionality to the add_task function
def add_task():
    task = input("Enter a task: ")

# TODO add the real functionality to the view_tasks function
def view_tasks():
    print("Tasks:")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")

def main():
    while True:
        print("What would you like to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print("")  # Print a blank line for spacing

if __name__ == "__main__":
    main()