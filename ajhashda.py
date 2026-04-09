import random
import os
home=0
hospoda=0
os.system("cls")

pozice=5
def funkce():
    global home
    global hospoda
    global pozice
    
    krok=random.choice(["+","-"])
    if krok=="+":
        pozice=pozice+1
    else:
        pozice=pozice-1
    if pozice ==0 :
        home=home+1
        pozice=5
    elif pozice==10:
        hospoda=hospoda+1
        pozice=5
    
    return pozice,home,hospoda




def opakovani():
    global pozice
    for i in range(100):
        pozice,home,hospoda=funkce()
        
    
    print(f"doma byl {home}x")
    print(f"v hospode byl {hospoda}x")
    


opakovani()