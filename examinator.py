import os
import random

def zisk_zadani(pocetotazek):
    """
    ukol funkce otevre slozku pokud existuje a nacte otazky
    pokud neexistuje konicprogream
    """    
    radky=[]
    
    try:
        with open("zadani.txt", "r", encoding="utf-8") as file:
            text=file.read()
            radky=text.splitlines()
            
            bloky= [radky[i:i+5] for i in range(0, len(radky),5)]
            random.shuffle(bloky)
            vybrane=bloky[:pocetotazek]
            return vybrane
        
    except FileNotFoundError:
        print("slozka s otazkami neexistuje")
    return []


def pocet_otazek():
    while True:
        try:
            pocetotazek=int(input(f"zadej kolik chces itazek 5-15"))
            
            if pocetotazek<5:
                print("minimum je pet")
                continue
            
            elif pocetotazek>15:
                print(f"maximum je 15")
                continue
            
            return pocetotazek
        
        except ValueError:
            print(f"spatny input")
            continue
        

def nacteni_otazek(vybrane):
    otazky=zisk_zadani(pocet_otazek)
    for blok in otazky:
        print("otazka:",blok[0])
        print("odpovedi:",blok[1:])
        try 

