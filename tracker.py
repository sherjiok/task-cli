import os
import sys
import json
import datetime

STATUS_LIST = ["todo","in-progress","done"]
DB_FILE = "tasks.json"

def write_json(data):    
    try:
        with open(DB_FILE,'w') as json_file:
            return json.dump(data, json_file, indent=4)
    except FileNotFoundError:
        return
    except PermissionError:
        print("Error: No tengo permisos para escribir en el archivo.")
        return
    except IOError as e:
        print(f"Error de escritura: {e}")    
        return

def read_json():
    try:
        with open(DB_FILE,'r')as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
        

def find_task(data, id):
    try:
        target_id = int(id)
    except ValueError:
        return
    for task in data:
        if task["id"] == target_id:
            return task
    return None
    
def add_task(description):    
    data = read_json()   
    
    task = create_task(data, description)
    
    data.append(task)    
    
    write_json(data)
    return task["id"]

def create_task(data, description):
    if not data:
        new_id = 1
    else:
        max_id = max(task["id"] for task in data)
        new_id = max_id + 1
    
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": None
    }
    
    return task

def update_task(id, new_data):
    
    data = read_json()
    
    task = find_task(data, id)    
    
    if not task:
        print(f"Task not found")
        return False
    
    task["description"] = new_data
    task["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_json(data)
    return True

def remove_task(id):
    data = read_json()
    
    task = find_task(data, id)
    
    if not task:
        print("Task not found")
        return False
    
    data.remove(task)
    write_json(data)
    return True 

def list_tasks():
    data = read_json()
    if not os.path.exists(DB_FILE) or data == []:
        print("No tasks found")
        return
    with open(DB_FILE,'r')as json_file:
        print(json_file.read())
        
def list_by_status(status):
    data = read_json()
    filtered = []
    for i in data:
        if i["status"] == status:
            filtered.append(i)
    print(filtered)

def update_status(new_status, id): 
    data = read_json()
    
    task = find_task(data, id)
    
    if not task:
        print("Task not found")
        return False
    task["status"] = new_status 
    task["updatedAt"] =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    
    write_json(data)
    
    return True

def show_help():
    print("""
    Task Manager CLI
        
    Commands:
        add <description>           Add a new task
        update <id> <description>   Update task description
        remove <id>                 Remove a task
        list                        List all tasks
        list [status]               List all tasks or filter by status
        mark <status> <id>          Change task status
        """)
        
def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['help', '-h', '--help']:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Usage: tracker.py add <task_description>")
                return
            description = " ".join(sys.argv[2:])
            new_id = add_task(description)
            print(f"Task added successfully (ID: {new_id})")
            
        elif command == "list":
            if len(sys.argv) >= 3:
                status = sys.argv[2]
                if status not in STATUS_LIST:
                    print("Invalid Status: todo, in-progress, done")
                    return
                else:
                    list_by_status(status)
            else:
                list_tasks()
        elif command == "update":
            if len(sys.argv) < 4:
                print("Usage: tracker.py update <task_id> <new_description>")
                return
            
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            
            if update_task(task_id, new_description):
                print("Task updated succesfully") 
        elif command == "remove":
            if len(sys.argv) < 3:
                print("Usage: tracker.py remove <task_id>")
                return
            else:
                task_id = sys.argv[2]
                if remove_task(task_id):
                    print("Task removed succesfully") 
        elif command == "mark":
            if len(sys.argv) < 4:
                print("Usage: tracker.py mark <task_status> <task_id>")
            else:
                new_status = sys.argv[2]
                task_id = sys.argv[3]
                if update_status(new_status, task_id):
                    print("Status updated succesfully")
        else:
            print(f"Unknown command: {command}\nUse -h, --help, help for help")
    except ValueError:
        print("Error: ID must be a number.")
    except Exception as e:
        print(f"Unexpected error: {e}")
            
main()


