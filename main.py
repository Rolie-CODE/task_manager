from asyncio import tasks
import json
class Task:
    def __init__(self,task_name):
        self.task_name = task_name

class Task__Manager():
    tasks = []
    def save_data(tasks):
        with open("tasks.json","w") as f:
            json.dump(tasks,f,indent=4)
    
    def load_data(tasks):     
        try:
            with open("tasks.json","r") as f:
                tasks = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            tasks = []

    def main__menu():
        print("1. Add Tasks")
        print("2. List Tasks")
        print("3. Remove Tasks")
        print("4. Back")

    def add_task(self, tasks):
        tasks.append(self.task_name)

    def list_tasks(tasks):
        return tasks
    
    def remove_task(self, tasks):
        if self.task_name in tasks:
            tasks.remove(f"{self.task_name}")
        else:
            return print(f"{self.task_name} not found in tasks")

Task__Manager.load_data(tasks)
while True:
    Task__Manager.main__menu()
    try:
        request = int(input(""))

    except ValueError:
        print("Enter a valid input!")
        break

    if request == 1:
        while True:
            task = input("Enter name of task(Q to quit): ").strip().lower()
            Task__Manager(task).add_task()
            Task__Manager.save_data()
            if task == "q":
                break

    elif request == 2:
        print(Task.list_tasks())
        input("Press Enter to continue...")

    elif request == 3:
        task = input("Enter name of task: ").strip().lower()
        Task__Manager(task).remove_task()
        Task__Manager.save_data()
        input("Press Enter to continue...")

    elif request == 4:
        print("Thank you for using the system")
        break

    else:
        print(f"{request} is an invalid input")

