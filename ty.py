import csv
import os
import math
import random

os.system('cls')
odpoved=input(f"chces si cisla volit sam? napis ano pokud chces jinak mas smulu\n")
if odpoved.lower()== "ano":
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
        
     
else:
    a= random.randrange(-100,100)
    b= random.randrange(-100,100)
    print(f"tva cisla byla {a,b}")   



vysledky=[]
vysledky.append (f"scitani {a+b}")
vysledky.append(f"odecitanui {a-b}")
vysledky.append(f"nadobeni {a*b}")
vysledky.append(f"mocnana {a**b}")

print(f"sciatni{a+b}")

print(f"Rozdíl: {a-b}")
print(f"Násobení: {a*b}")

if b !=0:
    print(a/b)
    vysledky.append(f"deleni{a/b}")
    vysledky.append("\n")
else:
     print(f"neni mozno delit nulou")

print(f"mocnana : {a**b}")

if a >=0: 
    print(f"Odmocnina z a: {a ** 0.5}")
    vysledky.append(f"odmocnina {a**0.5}")  
else:
    print(f"odmocninu neni mozno urcit")


with open("tabulka.csv","w",newline="",encoding="utf-8")as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(vysledky)
    