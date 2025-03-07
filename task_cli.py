import sys
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:  # Use "w" to write data to the file
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = max([task["id"] for task in tasks], default=0) + 1  # Generate a new ID
    task = {
        "id": task_id,
        "description": description,
        "status": "todo"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update a task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

# Mark a task as in progress
def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            save_tasks(tasks)
            print(f"Task {task_id} marked as in progress")
            return
    print(f"Task {task_id} not found")

# Mark a task as done
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print(f"Task {task_id} marked as done")
            return
    print(f"Task {task_id} not found")

# List all the tasks or tasks by status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Main function to handle command-line arguments
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: task-cli update <task_id> <new_description>")
            return
        task_id = int(sys.argv[2])
        new_description = " ".join(sys.argv[3:])
        update_task(task_id, new_description)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <task_id>")
            return
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <task_id>")
            return
        task_id = int(sys.argv[2])
        mark_in_progress(task_id)

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <task_id>")
            return
        task_id = int(sys.argv[2])
        mark_done(task_id)

    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)

    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
