# Metoda Monte Carlo pro odhad čísla π (pí)
# 
# Využívá náhodných čísel k simulaci experimentu s náhodnými body v čtverci, 
# do něhož je vepsán kruh. Poměr bodů, které padnou do kruhu, ku všem bodům ve čtverci, 
# odpovídá poměru ploch kruhu ku čtverci, z čehož lze vypočítat přibližnou hodnotu π.

""" 
Princip metody Monte Carlo pro výpočet π

1. Vezmeme čtverec o straně 2, tedy oblast od (-1, -1) do (1, 1) - random.uniform.
2. Do tohoto čtverce vepsáme kruh o poloměru 1 (střed v počátku).
3. Generujeme náhodné body v rámci čtverce.
4. Počítáme, kolik bodů spadlo do kruhu, tj. splňuje x^2 + y^2 <= 1.
5. Poměr bodů v kruhu ku všem bodům se blíží pi/4 (protože plocha kruhu je pi * 1^2 = pi) a plocha čtverce je 4).
6. Odhad čísla π pak získáme jako 4 * (bodů v kruhu/celkový počet bodů).


Zadání programové struktury

- Funkce `estimate_pi_monte_carlo(num_points: int) -> float`:
  - Parametr: počet náhodných bodů generovaných v čtverci.
  - Vrací odhad hodnoty π.

- Hlavní část programu (`__main__`):
  - Načte počet bodů od uživatele (např. pomocí `input()`).
  - Zavolá funkci `estimate_pi_monte_carlo`.
  - Vytiskne odhadnutou hodnotu π.
"""
import random
import os
os.system("cls")
my_list=[]
my_list1=[]


def randomnumber():
    
    
    y=random.uniform(-1,1)
    x=random.uniform(-1,1)
    z=(x**2+y**2)**0.5
    if z<=1:     
        my_list.append(1)
    elif z>0:
        my_list1.append(1)



def celek():
  """_summary_
  ma udelaz overeni vstupu
  a pocet bodu v kruhu

  Returns:
      _type_: _description_
  """  
  while True:
      try :
        n=int(input(f"zadejte pocet pokusu"))
          
      except ValueError:
          continue
      
      for i in range(n):
        randomnumber()
      x=len(my_list)
      
      print(f"cislo je {x}")
      print(f"cislo1 je {n}")
      return x,n


def cislopi(x,n):
    pi=(x/n)*4
    print(f"cilso pi je priblizne{pi}")
    return pi




x,n=celek()
pi=cislopi(x,n)

pii=3,14159
def overeni_pi(pi):
    pii=3.14159
    a=3.14159/pi
    print(f"{a*100}%shoda")
    return a


overeni_pi(pi)






