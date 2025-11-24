import random
import os 
os.system("cls")
random.seed()

def nahodne_cislo():
    """
    udelana nahodna cisla a vybere operaci 
    ktere pak jsou v returnu a pouzivaji se pri dalsich funkcich"""
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    volba=random.choice(["+","-","*","/"])
    print(f"jdeme pocitat talze tady jsou tva cisla {x} {volba} {y}")
    return x,y,volba

list=[]
list1=[]



def pocitani(x,y,volba):
    """zjisti vysledek od uzivatele pak ho poravna se pravsnou odpovedi 
    a zdle toho prida bod na lst spravnych nebo sparnych odpovedi"""
    while True:
        try :
            odpoved=float(input(f"jaky si myslis ze bude vysledek?"))
        except ValueError:
            print(f"zadej cislo")
            continue

        if volba=="+" :
            print(F"vyskedek scitani je{x+y}")

            if odpoved ==x+y:
                print(f"mas to spravne")
                list.append(1)
                break
            else:
                print(f"smula")
                list1.append(1)
                break


        if volba=="-" :
            print(F"vyskedek scitani je{x-y}")

            if odpoved ==x-y:
                print(f"mas to spravne")
                list.append(1)
                break
            else:
                print(f"smula")
                list1.append(1)
                break


        if volba=="*" :
            print(F"vyskedek scitani je{x*y}")

            if odpoved ==x*y:
                print(f"mas to spravne")
                list.append(1)
                break
            else:
                print(f"smula")
                list1.append(1)
                break


        if volba=="/" :
            if y==0:
                print(f"nulou nelze delit")
            else :
                print(F"vyskedek scitani je{x/y}")
                if odpoved ==x/y:
                    print(f"mas to spravne")
                    list.append(1)
                    break
                else:
                    print(f"smula")
                    list1.append(1)
                    break  

    return              
            
            


def volba():
    """ora se uzivatele zda chce pokracovat ukazuje po 
    skonceni listy s body"""
    while True:

        a=input(f"chces nejaky priklad pokud ano nepis nic a dej entr")
        
        if a=="":
            
            x, y, volba = nahodne_cislo()
            pocitani(x,y,volba)
            continue

        else :
            a=len(list)
            print(f"spravne odpovedi={a}")
            b=len(list1)
            print(f"spratne odpovedi={b}")
            break





volba()
