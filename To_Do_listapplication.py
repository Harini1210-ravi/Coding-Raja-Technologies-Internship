import os
import json
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def display_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks saved.")
    else:
        for idx, task in enumerate(tasks["tasks"], start=1):
            print(f"{idx}. {task['title']} - Priority: {task['priority']} - Due: {task.get('due_date', 'None')} - Status: {'Completed' if task['completed'] else 'Not yet Completed'}")

# Function to add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD) or leave empty: ")
    if due_date:
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
    tasks["tasks"].append({
        "title": title,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d") if due_date else None,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    choice = input("Enter the number of the task to remove: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(tasks["tasks"]):
            del tasks["tasks"][idx]
            save_tasks(tasks)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to mark a task as completed
def mark_as_completed(tasks):
    display_tasks(tasks)
    choice = input("Enter the number of the task to mark as completed: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(tasks["tasks"]):
            tasks["tasks"][idx]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\n****** To-Do List Menu *****")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_as_completed(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
