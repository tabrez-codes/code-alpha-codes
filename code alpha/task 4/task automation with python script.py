# Task: Automate a To-Do List with Due Dates

import datetime

class ToDoList:
    def __init__(self):
        # Initialize an empty dictionary to store tasks
        self.tasks = {}

    def add_task(self, task_name, due_date):
        # Try to parse the due date
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            # Add the task to the dictionary
            self.tasks[task_name] = due_date
            print(f"Task '{task_name}' added with due date {due_date}")
        except ValueError:
            # Handle invalid due date format
            print("Invalid due date format. Please use YYYY-MM-DD.")

    def view_tasks(self):
        # Check if there are any tasks
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            # Iterate over the tasks and print them
            for task, due_date in self.tasks.items():
                print(f"{task}: {due_date}")

    def delete_task(self, task_name):
        # Check if the task exists
        if task_name in self.tasks:
            # Delete the task
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted")
        else:
            print(f"Task '{task_name}' not found")

    def check_due_dates(self):
        # Get today's date
        today = datetime.date.today()
        # Check if there are any tasks
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Overdue Tasks:")
            # Use a list comprehension to find overdue tasks
            overdue_tasks = [task for task, due_date in self.tasks.items() if datetime.datetime.strptime(due_date, "%Y-%m-%d").date() < today]
            # Check if there are any overdue tasks
            if overdue_tasks:
                # Iterate over the overdue tasks and print them
                for task in overdue_tasks:
                    print(f"{task}: {self.tasks[task]}")
            else:
                print("No overdue tasks.")

def main():
    # Create a new To-Do List
    todo = ToDoList()

    while True:
        # Print the menu
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Check Due Dates")
        print("5. Quit")

        # Get the user's choice
        choice = input("Choose an option: ")

        if choice == "1":
            # Get the task name and due date
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            # Add the task
            todo.add_task(task_name, due_date)
        elif choice == "2":
            # View the tasks
            todo.view_tasks()
        elif choice == "3":
            # Get the task name to delete
            task_name = input("Enter task name to delete: ")
            # Delete the task
            todo.delete_task(task_name)
        elif choice == "4":
            # Check due dates
            todo.check_due_dates()
        elif choice == "5":
            # Quit the program
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()