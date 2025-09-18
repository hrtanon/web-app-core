import os
import math

os.system('cls')

# načítáme jako text (str), dokud to nejsou čísla
a = input("Zadej číslo, chlape: ")
b = input("Ještě jedno tě nezabije: ")

while not a.isdigit() or not b.isdigit():
    print("To není číslo!")
    a = input("Zadej číslo, chlape: ")
    b = input("Ještě jedno tě nezabije: ")

print("Takže čísla zadávat umíš!")

# tady už je jistota, že jsou to čísla, tak převedeme
a = int(a)
b = int(b)

# výpočty
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Nulou se dělit nedá!")

print(f"{a} ** {b} = {a ** b}")       # umocnění
print(f"odmocnina z {a} = {a ** 0.5}")  # druhá odmocnina
