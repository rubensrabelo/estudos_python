from model import Task, ToDoList
from utils import JSONFile, FolderHandling
# Adicionar uma task

task1 = Task("Excel")
task2 = Task("Correr")

to_do_list = ToDoList()
to_do_list.add_task(task1)
to_do_list.add_task(task2)

data_list = []
# Adicionar a task no DB
for task in to_do_list.tasks:
    data = {
        "name": task["name"],
        "status": task["status"].name
    }
    data_list.append(data)

JSONFile.save_in_json(data_list)
FolderHandling.saving_in_folder("db.json")
