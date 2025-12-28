## ⚡ task-cli

**A simple and efficient command-line interface for managing your daily tasks.**

## 📖 Overview

`task-cli` is a lightweight command-line utility designed to help you stay organized and productive. It provides a straightforward way to add, list, complete, and delete your tasks directly from your terminal, storing them locally for persistence. Perfect for developers, system administrators, or anyone who prefers a minimalist approach to task management.

## ✨ Features

-   **Add New Tasks**: Quickly add tasks with descriptive text.
-   **Update Tasks**: Update a task description using its ID.
-   **List All Tasks**: View your pending and completed tasks.
-   **List Tasks by Status**: Filter tasks by status.
-   **Mark Tasks Complete/In-Progres/Done**: Easily mark tasks as by their ID.
-   **Delete Specific Tasks**: Remove individual tasks that are no longer needed.
-   **Local Persistence**: Your tasks are saved locally and persist across sessions.

## 🚀 Quick Start

### Prerequisites
-   **Python 3.x**: Ensure you have Python 3 installed on your system.
    ```bash
    python3 --version
    ```

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/sherjiok/task-cli.git
    cd task-cli
    ```

2.  **Make the script executable**
    ```bash
    chmod +x tracker.py
    ```

### Usage

You can run the script directly.

#### Run Directly

```bash
python tracker.py help
```
### Basic Commands

```bash
# Display help information
python tracker.py -h
```

### Available Commands

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `add <description>` | Adds a new task. | `python tracker.py add "Buy groceries"` |
| `update <id> <new_description>` | Update task description | `python tracker.py update 1 "Refactor JSON storage"` |
| `list` | Lists all tasks (todo, in-progress and done). | `python tracker.py list` |
| `list <status>` | Lists tasks by status | `python tracker.py list in-progress` |
| `mark <status> <id>` | Change a task status using its ID. | `python tracker.py mark done 1` |
| `remove <id>` | Deletes a task by its ID. | `python tracker.py remove 2` |
| `help/-h/--help` | Shows the help message for the CLI tool. | `python tracker.py help` |

### Examples

```bash
# Add a new task
python tracker.py add "Review pull request #123"

# Add another task
python tracker.py add "Schedule team meeting for next week"

# List all current tasks
python tracker.py list

# Filter tasks by status
python tracker.py list todo

# Mark the first task as done (assuming it has ID 1)
python tracker.py done 1

# List tasks by status
python tracker.py list todo

# Delete a task by ID (assuming it has ID 2)
python tracker.py delete 2
```
##Project URL
https://roadmap.sh/projects/task-tracker
