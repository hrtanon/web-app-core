import csv
import os
import math
import random

os.system('cls')
odpoved=input(f"chces si cisla volit sam? napis ano pokud chces jinak mas smulu")
if odpoved== "ano":
     while True:
        a = input("Zadej číslo chlape: ")
        b = input("Ještě jedno tě nezabije: ")
        try:
            a = int(a)
            b = int(b)
            print("Takže čísla zadávat umíš!")
            break
        except ValueError:
            print("To není číslo! Zkus to znova.")
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

print(f"sciatni{a + b}")
print(a-b)
print(a*b)
if b !=0:
    print(a/b)
    vysledky.append(f"deleni{a/b}")
    vysledky.append("\n")
else:
     print(f"neni mozno delit nulou")

print(a**b)

if a >=0: 
    print(a**0.5)
    vysledky.append(f"odmocnina {a**0.5}")  
else:
    print(f"odmocninu neni mozno urcit")


with open("tabulka.csv","w",newline="",encoding="utf-8")as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(vysledky)
    