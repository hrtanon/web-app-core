import os
import math

os.system('cls')
odpoved=input(f"chces si cisla volit sam? napis ano pokud chces jinak mas smulu")
if odpoved== "ano":
     a=input(f"zadej cisla chlape")
     b=input(f"jeste jedno te nezabije")
     while not a.isdigit() or not b.isdigit():
        print(f"to neni cislo")
        a=input(f"zadej cisla chlape")
        b=input(f"jeste jedno te nezabije")
        if a.isdigit() and b.isdigit():
            print(f"takze cisla zadavt umis")
            break
else:
    a= random.randrange(-100,100)
    b= random.randrange(-100,100)
    print(f"tva cisla byla {a,b}")   

a=int(a)
b=int(b)

vysledky=[]
vysledky.append (f"scitani {a+b}")
vysledky.append(f"odecitanui {a-b}")
vysledky.append(f"nadobeni {a*b}")
vysledky.append(f"mocnana {a**b}")

print(f"{a + b}")
print(a-b)
print(a*b)
if b !=0:
    print(a/b)
    vysledky.append(f"deleni{a/b}")
    vysledky.append("\n")
else:
     print(f"neni mozno delit nulou")

print(a**b)

if a >0: 
    print(a**0.5)
    vysledky.append(f"odmocnina {a**0.5}")  
else:
    print(f"math error")


with open("tabulka.csv","w",newline="",encoding="utf-8")as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(vysledky)
    