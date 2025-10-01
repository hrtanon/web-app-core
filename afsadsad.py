import math
import os
import matplotlib.pyplot as plt 
os.system("cls")



def strany_trojuhelniku():
    # vyzada stranu kterou zadate pak je vraci jako a,b,c pokud lze trojuhelnik sestrojit 
    # kvuli tomu podminka if  a trouhelnikova nerovnost
    a=strana1=int(input(f"jaká je prvni strana?"))
    b=strana2=int(input(f"jaka je druha strana?"))
    c=strana3=int(input(f"jaka je treti strana?"))
    if a+b<c or a+c<b and c+b<a :
        print(f"nelze sestrojit trojuhelnik s techle stran")
    return a,b,c
    
trojuhelnik = strany_trojuhelniku()
print(trojuhelnik)

# ňefunguje print trojuhelnuku zjistit co tam chybi
