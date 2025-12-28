## ⚡ task-cli

**A simple and efficient command-line interface for managing your daily tasks.**

## 📖 Overview

`task-cli` is a lightweight, intuitive command-line utility designed to help you stay organized and productive. It provides a straightforward way to add, list, complete, and delete your tasks directly from your terminal, storing them locally for persistence. Perfect for developers, system administrators, or anyone who prefers a minimalist approach to task management.

## ✨ Features

-   **Add New Tasks**: Quickly add tasks with descriptive text.
-   **List All Tasks**: View your pending and completed tasks.
-   **Mark Tasks Complete**: Easily mark tasks as finished by their ID.
-   **Delete Specific Tasks**: Remove individual tasks that are no longer needed.
-   **Clear All Tasks**: Reset your task list by removing all entries.
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

You can run the script directly or create an alias for easier access.

#### Run Directly

```bash
./tracker.py help
```
### Basic Commands

```bash
# Display help information
task help
```

### Available Commands

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `add <description>` | Adds a new task. | `task add "Buy groceries"` |
| `list` / `ls` | Lists all tasks (pending and completed). | `task list` |
| `done <id>` | Marks a task as complete using its ID. | `task done 1` |
| `delete <id>` | Deletes a task by its ID. | `task delete 2` |
| `clear` | Clears all tasks from the list. | `task clear` |
| `report` | Displays a summary of pending vs. completed tasks. | `task report` |
| `help` | Shows the help message for the CLI tool. | `task help` |

### Examples

```bash
# Add a new task
task add "Review pull request #123"

# Add another task
task add "Schedule team meeting for next week"

# List all current tasks
task list

# Mark the first task as done (assuming it has ID 1)
task done 1

# View the updated list
task list

# See a summary report
task report

# Delete a task by ID (assuming it has ID 2)
task delete 2

# Clear all tasks
task clear
```
