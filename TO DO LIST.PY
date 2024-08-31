tasks = []

def display_tasks():
    """Display the list of tasks with their completion status."""
    if not tasks:
        print("No tasks to display.")
        return
    for i, task in enumerate(tasks):
        status = "[X]" if task['completed'] else "[ ]"
        print(f"{i + 1}. {status} {task['name']}")

def add_task():
    """Add a new task to the list."""
    name = input("Enter the task description: ")
    tasks.append({'name': name, 'completed': False})

def mark_task():
    """Mark a task as done or undone."""
    display_tasks()
    try:
        index = int(input("Enter the task number to toggle: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = not tasks[index]['completed']
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_task():
    """Remove a task from the list."""
    display_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the application."""
    while True:
        print("\nMenu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done/Undone")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
