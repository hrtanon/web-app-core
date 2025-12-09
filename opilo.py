import os
import random

list = []
a=5






def opila(a,list):
    
    
    n=10
    
    
    
    for i in range(n):
        list.append(".")
    krok=random.choice(["+","-"])
    if krok=="+":
        a=a+1
        list.pop(a)
        list.insert(a,"*")
        print(f"house{list}pub\n")
        
    
    elif krok=="-":
        a=a-1
        list.pop(a)
        list.insert(a,"*")
        print(f"house{list}pub\n")
        

    else :
        print(list)
        
    return list

for i in range (5):
    
    opila(a,list)
    list.clear()
    
