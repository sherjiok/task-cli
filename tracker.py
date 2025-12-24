import os
import sys
import json
import datetime

STATUS_LIST = ["todo","in-progress","done"]
DB_FILE = "tasks.json"

def write_json(data):    
    with open(DB_FILE,'w') as json_file:
        return json.dump(data, json_file, indent=4)

def read_json():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE,'r')as json_file:
        return json.load(json_file)

def find_task(data, id):
    for task in data:
        if task["id"] == int(id):
            return task
    return None
    
def add_task():    
    data = read_json()   

    task = create_task(data)
    if task == None:
        print("You must add a task description")
        return
    
    data.append(task)    
    
    write_json(data)
    print(f"Task added succesfully (ID: {data[-1]["id"] })") 
    return

def create_task(data):
    if len(sys.argv) < 3:
        return    
    
    if not data:
        new_id = 1
    else:
        last_id = data[-1]["id"]
        new_id = last_id +1
    
    description = " ".join(sys.argv[2:])
    
    task = {
        "id": new_id,
        "description": description,
        "status": STATUS_LIST[0],
        "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": None
    }
    
    return task

def update_task(id, new_data):
    
    if len(sys.argv) < 4:
        print("Usage: task-cli update <id> <new_description>")
        return    
    data = read_json()
    
    task = find_task(data, id)    
    
    if not task:
        print(f"Task not found")
        return
    
    task["description"] = new_data
    task["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_json(data)
    print(f"Task updated succesfully") 

def remove_task(id):
    data = read_json()
    
    task = find_task(data, id)
    
    if not task:
        print("Task not found")
        return
    
    data.remove(task)
    print("Task removed succesfully")
    write_json(data) 

def list_tasks():
    data = read_json()
    if not os.path.exists(DB_FILE) or data == []:
        print("No tasks found")
        return
    with open(DB_FILE,'r')as json_file:
        print(json_file.read())
        
def list_by_status(status):
    if status not in STATUS_LIST:
        print("invalid status: todo, in progress, done")
        return
    data = read_json()
    filtered = []
    for i in data:
        if i["status"] == status:
            filtered.append(i)
    print(filtered)

def update_status(new_status, id):
    if new_status not in STATUS_LIST:
        print("invalid status: todo, in-progress, done")
        return    
    data = read_json()
    
    task = find_task(data, id)
    
    if not task:
        print("Task not found")
        return
        
    task["status"] = new_status 
    task["updatedAt"] =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    write_json(data)
    
    return
        
def main():
    if len(sys.argv) < 2:
        return
    if sys.argv[1] == 'add':
        add_task()
    elif sys.argv[1] == 'update':
        update = " ".join(sys.argv[3:])
        update_task(sys.argv[2], update)
    elif sys.argv[1] == 'remove':
        remove_task(sys.argv[2])
    elif sys.argv[1] == 'list' and len(sys.argv) < 3:
        list_tasks()
    elif sys.argv[1] == 'list':
        list_by_status(sys.argv[2])
    elif sys.argv[1] == "mark":
        update_status(sys.argv[2], sys.argv[3])
    else:
        return
    
main()


