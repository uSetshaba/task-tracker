# Task Tracker CLI

https://roadmap.sh/projects/task-tracker

A simple, lightweight command-line interface (CLI) application to track and manage your tasks without any external dependencies.

## Overview

Task Tracker CLI is a command-line tool that helps you manage your to-do list by tracking what you need to do, what you're currently working on, and what you've completed. The application stores all tasks in a local JSON file and provides a straightforward interface for task management.

## Features

- Add new tasks with descriptions
- Update existing task descriptions
- Delete tasks when no longer needed
- Mark tasks as "in progress" or "done"
- List all tasks in your tracker
- Filter tasks by status (todo, in-progress, done)
- Automatic task metadata tracking (creation and update timestamps)
- Persistent storage in a local JSON file

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Make the script executable (Unix-based systems):

   ```bash
   chmod +x task-cli
   ```

3. (Optional) Add the directory to your PATH to access the tool from anywhere:
   ```bash
   # Add this line to your .bashrc, .zshrc, or similar shell configuration file
   export PATH="$PATH:/path/to/task-tracker-cli"
   ```

## Usage

### Adding a Task

```bash
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Updating a Task

```bash
task-cli update 1 "Buy groceries and cook dinner"
# Output: Task updated successfully
```

### Deleting a Task

```bash
task-cli delete 1
# Output: Task deleted successfully
```

### Changing Task Status

```bash
# Mark as in progress
task-cli mark-in-progress 1
# Output: Task marked as in-progress

# Mark as done
task-cli mark-done 1
# Output: Task marked as done
```

### Listing Tasks

```bash
# List all tasks
task-cli list
# Output: [List of all tasks with their details]

# List tasks by status
task-cli list todo
# Output: [List of tasks with todo status]

task-cli list in-progress
# Output: [List of tasks with in-progress status]

task-cli list done
# Output: [List of tasks with done status]
```

## Task Properties

Each task in the system has the following properties:

| Property      | Description                                       |
| ------------- | ------------------------------------------------- |
| `id`          | Unique identifier for the task                    |
| `description` | Text description of what needs to be done         |
| `status`      | Current status (`todo`, `in-progress`, or `done`) |
| `createdAt`   | Timestamp when the task was created               |
| `updatedAt`   | Timestamp when the task was last updated          |

## Technical Details

- Tasks are stored in a `tasks.json` file in the current directory
- The JSON file is created automatically if it doesn't exist
- No external libraries or frameworks are used
- All file operations use the native filesystem module
- Error handling is implemented for common scenarios (e.g., file not found, invalid input)

## Project Structure

```
task-tracker-cli/
├── task-cli         # Main executable script
├── tasks.json       # Data storage file (created on first run)
└── README.md        # This documentation
```

## Error Handling

The CLI handles various error scenarios gracefully:

- Invalid command or missing arguments
- Non-existent task IDs
- File access issues
- Invalid JSON data
- Concurrent access conflicts

## Development

### Requirements

- Any programming language of your choice
- Basic understanding of file I/O operations
- Knowledge of JSON data structure
- Command-line argument parsing

### Implementation Notes

- The application uses positional arguments to accept user inputs
- All data is persisted in a JSON file in the current working directory
- File operations are handled by the native filesystem module
- No external dependencies are required

## License

This project is licensed under the MIT License - see the LICENSE file for details.
