import math
import os
import matplotlib.pyplot as plt 
os.system("cls")


# ňesmim dat do parametnu urcuite veci kdyz pak chci aby byli dany az inputem

def strany_trojuhelniku():
    """

    vyzada stranu kterou zadate pak je vraci jako a,b,c pokud lze trojuhelnik sestrojit 
    return:
    kvuli tomu podminka if  a trouhelnikova nerovnost
    """
    while True:
     try:
        a = float(input("Jaká je první strana? "))
        b = float(input("Jaká je druhá strana? "))
        c = float(input("Jaká je třetí strana? "))
        
     except ValueError:
        print("Chyba! Zadej prosím číslo.")
        continue


     if a+b<c or a+c<b or c+b<a :
        print(f"nelze sestrojit trojuhelnik s techle stran")
        continue
    
     return a,b,c
def uhly_trojuhelniku(a,b,c):
    alfa = math.degrees(math.acos((b**2 + c **2 - a**2)/ (2*b*c)))
    bravo = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    charlie = math.degrees(math.acos((b**2+a**2-c**2)/(2*a*b)))
    return alfa, bravo , charlie

def obvod_a_obsah(a,b,c):
   obvod=a+b+c
   s=(a+b+c)/2
   obsah=(s*(s-a)*(s-b)*(s-c))**0.5
   return obvod, obsah

    


trojuhelnik = strany_trojuhelniku() 
a , b, c = trojuhelnik
uhly = uhly_trojuhelniku(a, b, c)
obvod,obsah =obvod_a_obsah(a, b, c)
print("Strany trojúhelníku:", (a, b, c))
print("Úhly trojúhelníku (stupně):", uhly)
print(f"obvod je--> {obvod,obsah}<---obsah")

