
tasks = []

def display_menu(): # Displays the main menu to the user. #
    print("\nMenu")
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Delete a task")
    print("4. Quit")

def add_task(): # adds new task to the todp list#
    task = input("enter task here:").strip() # Prompt User to enter task nad .strip out put #
    if task: # check if task string is not empty after .strip out-put #
        tasks.append(task) # Adding the cleaned task to (Tasks List)
        print(f"Task'{task}' added") # prints conformation message that includes the added task #
    else:
        print("Task can't be empthy.") # Prints message if imput is empty #

def view_tasks(): # Display a new task to the to-do list #
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task(): #  Deletes a task from the to-do list  #
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

def main(): # Function of main is to run the application #
    
    print("To-do list")
    while True:
        display_menu()
        try: 
            choice = int(input("Enter your choice:"))
            if choice == 1:
                 add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. please select a valid option.")
        except ValueError:
            print("invalid input. Please enter a number")


if __name__ == "__main__":
    main()

   


                 







