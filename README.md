Task Manager CLI (Python)

A simple command-line task tracker that stores tasks in a local JSON file.
Supports creating, updating, listing, filtering, and deleting tasks.

Requirements

Python 3.8+

No external dependencies

Installation

Download the script and place it in any folder:

tracker.py
tasks.json (auto-created)


Make the script executable (optional):

chmod +x tracker.py


Run using:

python tracker.py <command>

Commands
Command	Description
add <description>	Create a new task
list	List all tasks
list <status>	List tasks by status (todo, in-progress, done)
update <id> <description>	Update task description
mark <status> <id>	Change task status
remove <id>	Delete a task
help	Show help menu
Examples

Add a task:

python tracker.py add "Write project documentation"


List all tasks:

python tracker.py list


Filter by status:

python tracker.py list in-progress


Update a description:

python tracker.py update 2 "Refactor JSON storage"


Change status:

python tracker.py mark done 2


Remove a task:

python tracker.py remove 3

Data Storage

Tasks are saved in tasks.json with fields:

id, description, status, createdAt, updatedAt


The file is created automatically if it does not exist.

Notes

IDs must be numeric.

Valid statuses: todo, in-progress, done.
