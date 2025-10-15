# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
01_review_Jypyter_1-7.py
Vypracujte bez použití AI a připojení k netu. 12 úkolů.

VYPRACOVAL/A: 
-----------------------------------------------------------------
"""

import os

os.system("cls")
print("haloo")
##############################################################
# 1. Úkol: Základní aritmetické operace
# Napište kód, který bude načítat 2 čísla od uživatele (number1 a number2) a bude:
    # a) sčítat dvě načtená čísla (suma)
    # b) používat dělení a vracet jak běžné, tak celočíselné dělení (quotient, integer_division)

# Načtení čísel
def cisla():
    while True:
        try:
            a=float(input(f"prvni cislo"))
            b=float(input(f"druhe?"))
            
            
            
        except ValueError:
            print(f"zadej platne cislo")
            continue
        if b==0:
            print(f"nelze delit nulou")
            continue
        else :
            print(f"deleni{a/b}")
            print(f"bez zbytku{a//b}")
            break
    print(f"soucet{a+b}")
    return a,b
        
cisla()
    




# a) Sčítání


# b) Dělení a celočíselné dělení



##############################################################
# 2. Úkol: Exponenty
# Doplňte kód, který načte číslo od uživatele a:
# a) spočítá třetí odmocninu čísla
# b) spočítá druhou odmocninu čísla

# Načtení čísla


# a) Třetí odmocnina


# b) Druhá odmocnina
def mocnina():
    while True:
        try:
            a=float(input(f"prvni cislo"))
            b=float(input(f"druhe?"))
            
        except ValueError:
            print(f"zadej platne cislo")
            continue
        if b<=0 or a<=0:
            print(f"nelze delat odmocninu")
            continue
        else :
            print(f"treti odmocnina s a {a**(1/3)}")
            print(f"druha odmocnina s b{b**0.5}")
            break
    return
    
    
        




##############################################################
# 3. Úkol: Práce s proměnnými
# Zadejte proměnnou 'my_savings' a přiřaďte jí hodnotu od uživatele (např. 200)
# Poté vypočítejte, kolik budete mít peněz po přidání 10% úroků, které si uložíte do proměnné 'my_interest'.

def zidovstvi():
    my_savings=float(input(f"zadej tve uspory"))
    my_interest=my_savings+(my_savings*0.1)
    return my_interest

##############################################################
# 4. Úkol: Operace s řetězci
# Napište kód, který:
    # a) načte dva řetězce od uživatele (string1 a string2)
    # b) zkontroluje, zda jsou oba řetězce stejné délky
    # c) spojí oba řetězce do jednoho a vypíše výsledek

# a) Načtení řetězců
def retez():
    ret=input(f"zadej neco")
    a=len(ret)
    ez=input(f"zadej neco dalsiho stejne delky")
    b=len(ez)
    if a==b:
        print(f"reteze byli stejen  dobra pracve")
    elif a <b:
        print(f"hohohho prvni byl kratsi")
    else:
        print(f"druhy byl trochu kratsi chlape")
    print(f"obe zprravy dohgromady{ret+ez}")

# b) Zkontrolujte délku řetězců


# c) Spojení řetězců


has 
##############################################################
# 5. Úkol: Práce s cykly
# Napište kód, který:
    # a) načte číslo od uživatele (např. 16)
    # b) vypíše všechna čísla od 1 do tohoto čísla
    # c) na každém pátém čísle vypíše text "Pátý krok!"

# Načtení čísla


# b) Výpis čísel



##############################################################
# 6. Úkol: Slovníky v Pythonu
# Napište kód, který:
    # a) vytvoří prázdný slovník "person"
    # b) přidá do slovníku tři položky, které načte od uživatele (např. name, age, city)
    # c) vypíše všechny klíče a hodnoty slovníku v cyklu

# a) Vytvoření slovníku:
def slovnik():
    jmeno=input("jmeno?")
    vek=input("vek?")
    mesto=input("mesto?")
    my_dict={'key1':jmeno,'key2':vek,'key3':mesto}
    print(my_dict['key1'])
    print(my_dict['key2'])
    print(my_dict['key3'])


# b) Načtení údajů od uživatele


# Přidání údajů do slovníku


# c) Výpis slovníku



##############################################################
# 7. Úkol: Použití f-string
# Napište kód, který načte dva číselné údaje (např. result, score) a poté:
    # a) použije f-string pro vložení těchto hodnot do textu
    # b) použije f-string pro zobrazení těchto hodnot s přesností na 2 desetinná místa

# Načtení čísel


# a) Použití f-string


# b) Použití f-string s přesností na 2 desetinná místa



##############################################################
# 8. Úkol: Vytváření seznamů a indexování
# Napište kód, který:
    # a) vytvoří seznam my_list o pěti prvcích na základě vstupu od uživatele
    # b) vypíše třetí prvek seznamu
    # c) vypíše poslední dva prvky seznamu

# a) Vytvoření seznamu


# b) Třetí prvek


# c) Poslední dva prvky



##############################################################
# 9. Úkol: Základní metody seznamu
# Napište kód, který:
    # a) vytvoří seznam my_list o třech prvcích od uživatele a přidá nový prvek pomocí metody append() + zobrazí
    # b) odstraní prvek z určeného indexu od uživatele, pomocí metody pop() + zobrazí
    # c) seřadí seznam abecedně pomocí metody sort() + zobrazí

# a) Vytvoření seznamu a přidání nového prvku

def seznamnajdutamconeznam():
    my_list=[]
    for i in range(3):
        prvek=input(f"tri prvky" )
        my_list.append(prvek)
    print(my_list) 
    a=input(f"zadej 0 nebo 1 nebo 2")
    my_list.pop(0)
    print(my_list) 
    my_list.sort()
    print(my_list) 
# b) Odstranění prvku na zvoleném indexu

seznamnajdutamconeznam()
# c) Seřazení seznamu



##############################################################
# 10. Úkol: Vytvoření tuple a indexování
# Napište kód, který:
    # a) vytvoří tuple my_tuple se třemi prvky na základě vstupu od uživatele
    # b) vypíše první prvek tohoto tuple
    # c) vypíše poslední prvek tohoto tuple

# a) Vytvoření tuple

def tuple():
    a,b,c=ale=input("neco 3 cisla bez mezer")
    print(f"prvni prvek{a}")
    print(f"posledni prvek{c}")
    

# b) První prvek


# c) Poslední prvek



##############################################################
# 11. Úkol: Základní metody pro tuple
# Napište kód, který:
    # a) vytvoří tuple my_tuple, který bude obsahovat následující prvky: 1, 2, 3, 2, 4, 2, 5
    #    a spočítá počet výskytů uživatelem zadaného prvku pomocí metody count()
    # b) zjistí index uživatelem zadaného prvku element_to_find v tuplu my_tuple pomocí metody index()

# a) Vytvoření tuple a použití metody count()


# b) Použití metody index()



##############################################################
# 12. Úkol: Neměnnost tuple
# Napište kód, který:
    # a) vytvoří tuple a pokusí se změnit jeden z jeho prvků (tím demonstruje chybu)
    # b) dokáže zachytit tuto chybu a informovat uživatele o chybě

# a) Vytvoření tuple


# b) Pokus o změnu prvku



##############################################################

## NEZAPOMEŇTE ZMĚNIT JMÉNO SOUBORU! ##