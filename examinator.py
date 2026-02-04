import os
import random
from datetime import datetime
spravne_ospovedi=[]
spatne_ospovedi=[]
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


def nacteni_otazek(pocetotazek):
    otazky=zisk_zadani(pocetotazek)
    for blok in otazky:
        print("otazka:",blok[0])
        odpovedi=blok[1:]
        random.shuffle(odpovedi)
        
        for i,moznost in enumerate(odpovedi,start=1):
            print(f"{i}) {moznost}")
            
        
        while True:
            try :
                odpoved=int(input("zadej odpoved"))
                return odpoved , odpovedi ,blok
            
            except ValueError:
                print("zadej pozadovany vstup")
                continue


def overeni_odpovedi_spravne(odpovedi):
    
    try:
        for i in range(len(odpovedi)):
            odpoved=odpovedi[i]
            casti=odpoved.split(";")
            if casti[0]=="1":
                spravna_odpoved=casti[1]
                return spravna_odpoved
            
    
    except ValueError:
        return []
        

    
def shoda_odpovedi(odpoved,spravna_odpoved,blok):
    
    """_summary_ urci zda tazajici spravne odpovedel na otazku
    Returns:
        spatne odpoveedi a sparvne odpovedi a soubor spatne zodpovezene otazky
    """
    
    if odpoved==spravna_odpoved:
        spravne_odpovedi=spravne_odpovedi+1
        return spravne_odpovedi

    elif odpoved!=spravna_odpoved:
        spatne_odpovedi=spatne_odpovedi+1
        with open("spatneodpovedi.txt", "a", encoding="utf-8") as File:
            File.write(f"{blok} \n @")
        return spatne_odpovedi




def uspesnost(pocet_odpovedi,spravne_odpovedi):
    uspech = spravne_odpovedi / pocet_odpovedi * 100  # v procentech
    
    if uspech > 90:
        print(f"Úspěšnost = {uspech:.1f} %, známka: 1")
    elif 75 <= uspech <= 89:
        print(f"Úspěšnost = {uspech:.1f} %, známka: 2")
    elif 60 <= uspech <= 74:
        print(f"Úspěšnost = {uspech:.1f} %, známka: 3")
    elif 45 <= uspech <= 59:
        print(f"Úspěšnost = {uspech:.1f} %, známka: 4")
    else:  
        print(f"Úspěšnost = {uspech:.1f} %, známka: 5")
    return uspech

def zisk_jmena():
    while True:
        try:
            jmeno=str(input("zadej jmeno"))
            print(f"jmeno zkouseneho {jmeno}")
            return jmeno
        except ValueError:
            print("spatny vstup")
            continue

def volba():
    while True:
        try:
            volba=int(input("1-nová hra \n 2-konec"))
            if volba<1 or volba>2:
                continue
            else:
                return volba
        except ValueError:
            print("neplatny vstup")
            continue


def menu():
    print("Načítám otázky z adresáře 'zadani_otazek'")
    print(f"Načteno 15 otázek ze souboru zadani")
    zisk_jmena()
    pocetotazek=pocet_otazek()
    print("test pripraven")
    for i in range(pocet_otazek):
        odpoved,odpovedi,blok=nacteni_otazek()
        spravnaodpoved=overeni_odpovedi_spravne(int(pocetotazek))
        spravneodpovedi=shoda_odpovedi(odpoved,spravnaodpoved,blok)
        os.system("cls")
    uspesnost(pocetotazek,spravneodpovedi)
    


def realne_menu():
    volb=volba()
    
    if volb==1:
        menu()
        
    elif volb==2:
        print("nekdy priste")
        











realne_menu()




def uloz_vysledek(jmeno, prijmeni, pocet_otazek, spravne_odpovedi, spatne_otazky):
    
    if not os.path.exists("Vysledky_testu"):
        os.makedirs("Vysledky_testu")

    now = datetime.now()
    datum_soubor = now.strftime("%Y%m%d_%H%M%S")

    #
    jmeno_norm = jmeno.lower().replace(" ", "_")
    prijmeni_norm = prijmeni.lower().replace(" ", "_")

    
    procenta = spravne_odpovedi / pocet_otazek * 100
    if procenta >= 90:
        znamka = 1
    elif procenta >= 75:
        znamka = 2
    elif procenta >= 60:
        znamka = 3
    elif procenta >= 45:
        znamka = 4
    else:
        znamka = 5

    nazev_souboru = f"{prijmeni_norm}_{jmeno_norm}_{datum_soubor}_{pocet_otazek}_{znamka}.txt"
    cesta = os.path.join("Vysledky_testu", nazev_souboru)

    with open(cesta, "w", encoding="utf-8") as f:
        f.write(f"Vypracoval/a: {jmeno} {prijmeni}\n")
        f.write(f"Otázek v testu: {pocet_otazek}\n")
        f.write(f"Výsledná známka: {znamka}\n")
        f.write(f"Procentní úspěšnost: {procenta:.1f} %\n")
        f.write("Stupnice: <100-90>,(90-75>,(75-60>,(60-45>,(45-0>\n")
        f.write(f"Datum a čas vyhodnocení: {now.day}.{now.month}.{now.year}, {now.hour}:{now.minute}:{now.second}\n\n")
        f.write("----------------------\n")
        f.write("Chybně zodpovězeno:\n\n")

        
        for blok in spatne_otazky:
            for radek in blok:
                f.write(radek + "\n")
            f.write("\n")

    print(f"Výsledek uložen do: {cesta}")