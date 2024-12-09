tasks = []  # Global list to store tasks

def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter task here: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added.")
    else:
        print("Task can't be empty.")

def view_tasks():
    """Displays tasks from the to-do list."""
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task():
    """Deletes a task from the to-do list."""
    if tasks:
        try:
            view_tasks()
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")
