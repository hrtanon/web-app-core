from modules.task import Task 
import json
import os


ALOWEDSTATUS=["todo","in progrss","done"]


class Taskmanage():
    def __init__(self):
        self.tasks=[]
        self.next_id=1
        
    def novy_task(self):
        task_id=self.next_id
        self.next_id+=1
        title=input("zadej title")
        des=input("zadej description")
        status=input("zadej status")
        task=Task(id,title,des,status)
        self.tasks.append(task)
        return task
    
    def seznam(self):
        print(f"{self.tasks}")
    
    def seznam_dlestatus(self,status):
        task_status=[]
        for task in self.tasks:
            if task.status==status:
                task_status.append(task)
        return task_status
    
    def najit(self,id):
        for task in self.tasks:
            if task.task_id==id:
                
                return task
            else:
                return None
        
    
    def uprav(self,task_id,
            title: str | None = None,
            descriprion: str | None = None):
        task=self.najit(task_id)
        if title is not None:
            task.change_title(title)
        if descriprion is not None:
            task.change_discription(descriprion)
        return task
    
    def zmena_status_dleid(self,task_id,status:str):
        if status != ALOWEDSTATUS:
            print("neplatny status")
        else:
            task=self.najit(task_id)
            task.change_status(status)
            return task
    
    def smaz(self,task_id):
        task=self.najit(task_id)
        self.tasks.remove(task)
        print("task smazan")
    
    def save_jas(self,path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,"w", encoding="utf-8")as File:
            task_data=[]
            json.dump([t.to_dict() for t in self.tasks], File)
    
    def from_jas(self,path):
        if not os.path.exists(path):
            return
        with open(path,"r",encoding="utf-8")as File:
            data=[]
            data=json.load(File)
            for item in data:
                self.tasks.append(Task.from_dic(item))
        if self.tasks:
            self.next_id=max(task.task_id for task in self.tasks)+1
            