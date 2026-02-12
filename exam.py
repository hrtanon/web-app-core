import os
import random
from datetime import datetime

# Globální seznamy pro sběr výsledků
spravne_odpovedi = 0  # místo listu používám integer
spatne_odpovedi = 0
spatne_otazky = []

# -----------------------------
# Funkce pro načtení otázek
# -----------------------------
def zisk_zadani(pocetotazek):
    try:
        with open("zadani.txt", "r", encoding="utf-8") as file:
            radky = file.read().splitlines()
            bloky = [radky[i:i+5] for i in range(0, len(radky), 5)]
            random.shuffle(bloky)
            vybrane = bloky[:pocetotazek]
            return vybrane
    except FileNotFoundError:
        print("Slozka s otazkami neexistuje")
        return []

# -----------------------------
# Funkce pro zadání počtu otázek
# -----------------------------
def pocet_otazek():
    while True:
        try:
            pocet = int(input("Zadej kolik chces otazek (5-15): "))
            if pocet < 5:
                print("Minimum je 5")
            elif pocet > 15:
                print("Maximum je 15")
            else:
                return pocet
        except ValueError:
            print("Spatny vstup, zadej cislo.")

# -----------------------------
# Funkce pro získání jména
# -----------------------------
def zisk_jmena():
    while True:
        jmeno = input("Zadej jmeno: ").strip()
        if jmeno:
            print(f"Jmeno zkouseneho: {jmeno}")
            return jmeno
        else:
            print("Neplatny vstup.")

# -----------------------------
# Funkce pro získání správné odpovědi
# -----------------------------
def overeni_odpovedi_spravne(odpovedi):
    for odpoved in odpovedi:
        casti = odpoved.split(";")
        if casti[0] == "1":
            return casti[1]
    return None

# -----------------------------
# Funkce pro testování otázek
# -----------------------------
def nacteni_otazek(pocetotazek):
    global spravne_odpovedi, spatne_odpovedi, spatne_otazky
    otazky = zisk_zadani(pocetotazek)
    
    for cislo_otazky, blok in enumerate(otazky, start=1):
        os.system("cls")  # vycistit terminal
        print(f"Otázka {cislo_otazky}/{pocetotazek}: {blok[0]}")
        odpovedi = blok[1:]
        random.shuffle(odpovedi)
        
        for idx, moznost in enumerate(odpovedi, start=1):
            print(f"{idx}) {moznost}")
        
        while True:
            try:
                odpoved = int(input("Zadej odpoved (cislo): "))
                if 1 <= odpoved <= len(odpovedi):
                    break
                else:
                    print("Spatny vyber, zadej cislo odpovedi.")
            except ValueError:
                print("Spatny vstup, zadej cislo.")

        spravna_odpoved = overeni_odpovedi_spravne(odpovedi)
        vybrana_odpoved = odpovedi[odpoved - 1].split(";")[1]

        if vybrana_odpoved == spravna_odpoved:
            spravne_odpovedi += 1
        else:
            spatne_odpovedi += 1
            spatne_otazky.append(blok)

# -----------------------------
# Funkce pro vyhodnocení úspěšnosti
# -----------------------------
def uspesnost(pocet_otazek):
    global spravne_odpovedi
    uspech = spravne_odpovedi / pocet_otazek * 100
    if uspech >= 90:
        znamka = 1
    elif uspech >= 75:
        znamka = 2
    elif uspech >= 60:
        znamka = 3
    elif uspech >= 45:
        znamka = 4
    else:
        znamka = 5
    print(f"Úspěšnost: {uspech:.1f} %, známka: {znamka}")
    return uspech, znamka

# -----------------------------
# Funkce pro uložení výsledku
# -----------------------------
def uloz_vysledek(jmeno, prijmeni, pocet_otazek, spravne_odpovedi, spatne_otazky):
    if not os.path.exists("Vysledky_testu"):
        os.makedirs("Vysledky_testu")

    now = datetime.now()
    datum_soubor = now.strftime("%Y%m%d_%H%M%S")

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

# -----------------------------
# Menu
# -----------------------------
def menu():
    global spravne_odpovedi, spatne_odpovedi, spatne_otazky
    spravne_odpovedi = 0
    spatne_odpovedi = 0
    spatne_otazky = []

    print("Načítám otázky z adresáře 'zadani_otazek'")
    jmeno = zisk_jmena()
    prijmeni = input("Zadej prijmeni: ").strip()
    pocet = pocet_otazek()
    print("Test pripraven. Zacina...")

    nacteni_otazek(pocet)
    uspesnost(pocet)
    uloz_vysledek(jmeno, prijmeni, pocet, spravne_odpovedi, spatne_otazky)

# -----------------------------
# Volba
# -----------------------------
def volba():
    while True:
        try:
            v = int(input("1-nová hra \n2-konec\n"))
            if v in [1,2]:
                return v
        except ValueError:
            print("Neplatny vstup.")

def realne_menu():
    while True:
        choice = volba()
        if choice == 1:
            menu()
        else:
            print("Nekdy priste")
            break

# -----------------------------
# Start programu
# -----------------------------
realne_menu()
