# Simple To-Do List Application

FILE_NAME = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    tasks = []
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        pass  # If the file doesn't exist, start with an empty list
    return tasks


# Function to save tasks to the file
def save_tasks(tasks):
    file = open(FILE_NAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()


# Function to view tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        i = 0
        for task in tasks:
            print(str(i + 1) + ". " + task)
            i = i + 1


# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task == "":
        print("Task cannot be empty.")
    else:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")


# Function to remove a task
def remove_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to remove.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task removed:", removed_task)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main function with menu and exit confirmation
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Ask user whether to continue or exit
        continue_choice = input("\nDo you want to continue? (y/n): ").strip().lower()
        if continue_choice == 'n':
            print("Goodbye!")
            break


# Start the program
if __name__ == "__main__":
    main()