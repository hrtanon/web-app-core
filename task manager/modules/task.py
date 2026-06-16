import random
import os



class Task():
    def __init__(self,title_id,title,description,status):
        self.status=status
        self.title=title
        self.title_id=title_id
        self.description=description 
    def __str__(self):
        return f"{self.title_id},{self.title},{self.status},{self.description}"
    
    def change_status(self,new_status):
        povolene_statusy=["todo","in progrss","done"]
        if  new_status in povolene_statusy:
            self.status=new_status
        else:
            print(f"neplatny status")
    
    def change_title(self):
        while True:
        
            try :
                new_name=str(input("zadej nove jmeno"))
                if new_name=="":
                    print("zadej neco")
                    continue
                
                else:
                    self.title=new_name
                    print("jmeno bylo zmeneno")
                    return 
        
            except ValueError:
                print("valueerror")
                continue
    
    
    
    def change_discription(self):
        while True:
        
            try :
                new_discription=str(input("zadej novy popis"))
                self.description=new_discription
                print("jmeno bylo zmeneno")
                return 
        
            except ValueError:
                print("valueerror")
                continue
    
    def to_dic(self):
        my_dic={
            "title":self.title,
            "title_id":self.title_id,
            "status":self.status,
            "description":self.description
            }
        return my_dic
    
    
    @staticmethod
    def from_dic(my_dic):
        title=my_dic["title"]
        title_id=my_dic["title_id"]
        status=my_dic["status"]
        description=my_dic["description"]
        return Task(title_id,title,status,description)
    
    
