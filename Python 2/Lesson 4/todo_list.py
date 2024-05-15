# To-do-list Manager

# Function to initilize an empty to-do list
def initialize_todo_list():
    return []

# Function to add task to my to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to Summer's list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed from Summer's list.")
    else:
        print(f"Task '{task}' not found in Summer's list.")


# Function to display the to-do list
def display_todo_list(todo_list):
    if todo_list:
        print("Current To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}: {task}")
    else:
        print("Your to-do list is empty.")

# Function to mark a task as complete
def complete_task(todo_list, task):
    if task in todo_list:
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in Summer's list.")
