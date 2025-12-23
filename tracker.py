import os
import sys
import json
import datetime

status = ["todo","in progress","done"]

def write_json(data):    
    with open('tasks.json','w') as json_file:
        return json.dump(data, json_file, indent=4)

def read_json():
    if not os.path.exists("tasks.json"):
        return []
    with open('tasks.json','r')as json_file:
        return json.load(json_file)
    
def add_task():    
    data = read_json()   

    data.append(create_task(data))    
    
    write_json(data)
    print("Task added succesfully") 
    return

def create_task(data):
    if not data:
        new_id = 1
    else:
        last_id = data[-1]["id"]
        new_id = last_id +1
    
    if len(sys.argv) < 3:
        print("You must add a task name")
        return
    
    description = " ".join(sys.argv[3:])
    
    task = {
        "id": new_id,
        "name": sys.argv[2],
        "description": description,
        "status": status[0],
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": None
    }
    
    return task
    

def update_task():
    return

def delete():
    return

def listar():
    return
        
def main():
    if len(sys.argv) < 2:
        return
    if sys.argv[1] == 'add':
        add_task()
    elif sys.argv[1] == 'update':
        update_task()
    elif sys.argv[1] == 'delete':
        delete()
    elif sys.argv[1] == 'list':
        listar()
    else:
        print("Invalid argument")
        return
    
main()


