CLI Task Tracker

A simple command-line application to manage tasks, storing data in a local JSON file.
Requirements

    Python 3.x

Usage

Run the script from your terminal:
python tracker.py <command> [arguments]

Commands
Command	Usage	Description
Add	add "Task description"	Create a new task.
Update	update <id> "New text"	Update a task's description.
Delete	remove <id>	Delete a task by ID.
Mark	mark <status> <id>	Change status (todo, in-progress, done).
List	list	View all tasks.
Filter	list <status>	View tasks by status.
Help	help	Show available commands.

Example
python tracker.py add "Finish the report"
python tracker.py mark in-progress 1
python tracker.py list
