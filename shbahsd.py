import random

def pohyb_opilce(pozice, pole):
    krok = random.choice(["+", "-"])
    
    
    pole[pozice] = "."
    
    if krok == "+" and pozice < len(pole) - 1:
        pozice += 1
    elif krok == "-" and pozice > 0:
        pozice -= 1
    
        
    
    pole[pozice] = "*"
    print("".join(pole))
    
    
    
    return pozice


pole =["."] * 11  
a = 5
pole[a] = "*"

for _ in range(100):
    a = pohyb_opilce(a, pole)
    if a == 10 or 0:
        print("dosel nekam")
        print(_,"kroku")
        break
    
    