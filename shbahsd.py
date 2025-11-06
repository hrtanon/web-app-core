import random

def pohyb_opilce(pozice, pole):
    krok = random.choice(["+", "-"])
    
    # vymaž starou pozici
    pole[pozice] = "."
    
    if krok == "+" and pozice < len(pole) - 1:
        pozice += 1
    elif krok == "-" and pozice > 0:
        pozice -= 1
    
    # označ novou pozici
    pole[pozice] = "*"
    print("".join(pole))
    
    return pozice

# inicializace
pole = ["."] * 10
a = 5
pole[a] = "*"

for _ in range(10):
    a = pohyb_opilce(a, pole)
