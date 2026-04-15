# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Vesmirny obchodnik – pracovni verze (empty).

Implementuj textovou hru o obchodovani mezi planetami.
Hrac nakupuje zbozi levne na jedne planet a prodava draze na jine.
Pri kazde ceste nastane nahodna udalost.
Stav hry se uklada do JSON souboru.

Obsah:
- CAST 1: Konstanty (zbozi, planety, udalosti, nastaveni hry)
- CAST 2: Inicializace a ukladani hry (new_game, load_game, save_game)
- CAST 3: Herni logika (cargo_used, generate_event, apply_event, travel)
- CAST 4: Nakup a prodej (buy_goods, sell_goods)
- CAST 5: Zobrazeni (clear, print_status)
- CAST 6: Hlavni smycka (main)
"""

import json
import os
import random

SAVE_FILE = "save_game_trader.json"


##############################################################
### CAST 1: Konstanty
##############################################################

# TODO: Vytvor slovnik GOODS kde klic je ID zbozi (napr. "food")
#       a hodnota je slovnik s klicem "name" (zobrazovany nazev).
#       Pridej zbozi: food (Potraviny), minerals (Mineraly), tech (Technika).
GOODS = {"food":{"potraviny"}, "minerals" :("Mineraly"), "tech" : ("Technika")}

# TODO: Vytvor slovnik PLANETS kde klic je ID planety (napr. "terra")
#       a hodnota je slovnik s klici "name" a "prices".
#       "prices" je slovnik {good_id: cena_v_kreditech}.
#       Pridej planety: terra, mars, nexus s cenami podle readme.
PLANETS = {"teraa":{
    "name": "teraa",
    "cena":{"food": 10, "minerals": 35, "tech": 55}
    } ,"mars":{"name":"mars", "cena":{{"food": 10, "minerals": 35, "tech": 55},
}},"nexus":{"name":"nexus", "cena":{{"food": 10, "minerals": 35, "tech": 55},
}}
}

# TODO: Vytvor slovnik EVENTS kde klic je ID udalosti (napr. "pirates")
#       a hodnota je slovnik s klici "name" a "weight".
#       Soucet vsech "weight" musi byt 1.0.
#       Pridej udalosti: pirates (0.20), asteroid (0.25), smooth (0.55).
EVENTS = {
    "pirates":{"name":" pirates","problerm":"-80zl","weight":0.2},
    "bombaa":{"name":" bombaa","problerm":"3ks zbozi ","weight":0.25},
    "smoth":{"name":" smoth","problerm":"15zl","weight":0.55}
}

# TODO: Definuj tyto konstanty se spravnymi hodnotami:
CARGO_CAPACITY   = 20   # maximalni pocet kusu v nakladu celkem
STARTING_CREDITS = 500   # pocatecni kredity hrace
TARGET_CREDITS   = 2000  # pocet kreditu potrebnych k vitezstvi
PIRATE_LOSS      = 80 # kredity ztracene pri prepadeni piraty


##############################################################
### CAST 2: Inicializace a ukladani hry
##############################################################

def new_game():
    """Vytvori a vrati slovnik reprezentujici novou hru.

    Returns:
        Slovnik s klici: "day" (1), "credits" (STARTING_CREDITS),
        "location" ("terra"), "cargo" (prazdny slovnik).
    """
    # TODO: Vrat slovnik se vsemi klici nove hry.
    game= { 
    "day":      1,
    "credits":  500,
    "location": "terra",   # ID aktuální planety
    "cargo":    {}
    }
    return game
    raise NotImplementedError


def load_game():
    """Nacte hru ze souboru SAVE_FILE, nebo vytvori novou hru.

    Returns:
        Nacteny nebo novy game slovnik.
    """
    if os.path.exists:
        with open (SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
            
    # TODO: Pouzij os.path.exists() pro kontrolu existence souboru.
    # TODO: Pokud soubor existuje, otevri ho, nacti JSON a vrat slovnik.
    # TODO: Pokud neexistuje, vrat new_game().
    
    return new_game()
    raise NotImplementedError


def save_game(game):
    """Ulozi game slovnik do souboru SAVE_FILE ve formatu JSON.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    with open(SAVE_FILE, "w" ,encoding="utf-8")as f:
        json.dump(game,f,indent=2,ensure_ascii=False)
    # TODO: Otevri SAVE_FILE pro zapis (mod "w") s kodovanim utf-8.
    # TODO: Pouzij json.dump() pro ulozeni slovniku game. Nastav indent=2.
    raise NotImplementedError


##############################################################
### CAST 3: Herni logika
##############################################################

def cargo_used(game):
    """Vrati celkovy pocet kusu zbozi v nakladu.

    Returns:
        Cele cislo – soucet vsech hodnot v game["cargo"].
    """
    return sum(game["cargo"].values())
    # TODO: Vrat soucet vsech hodnot v game["cargo"].
    #       Tip: pouzij sum() a .values(). Funguje i pro prazdny slovnik.
    raise NotImplementedError


def generate_event():
    """Nahodne vybere ID udalosti podle vah definovanych v EVENTS.

    Returns:
        Retezec – ID udalosti (napr. "pirates").
    """
    ids= list(EVENTS.keys())
    weights=[EVENTS[e]["weight"] for e in ids]
    
    event=random.choices(ids,weights=weights,k=1)[0]
    return event# TODO: Ziskej seznam ID udalosti a seznam jejich vah z EVENTS.
    # TODO: Pouzij random.choices(ids, weights=vahy, k=1)[0] a vrat vysledek.
    raise NotImplementedError


def apply_event(game, event_id):
    """Aplikuje efekt udalosti na stav hry.

    Efekty:
      "pirates"  – hrac ztrati min(PIRATE_LOSS, game["credits"]) kreditu
      "asteroid" – pokud je misto v nakladu, hrac ziska az 3 ks nahodneho zbozi
      "smooth"   – hrac ziska 15 kreditu

    Args:
        game:     Slovnik s aktualnim stavem hry.
        event_id: ID udalosti (retezec).

    Returns:
        Retezec s popisem toho, co se stalo (zobrazi se hracovi).
    """
    # TODO: Implementuj vetev pro "pirates":
    #loss = min(PIRATE_LOSS, game["credits"])
    #         Odecti loss od game["credits"], vrat popis.
    # TODO: Implementuj vetev pro "asteroid":
    if event_id=="pirates":
        
        loss= min(PIRATE_LOSS,game["credits"])
        game["credits"]=game["credits"]-loss
        return "utok piraty"
        
    elif event_id=="asteroid":
        misto=CARGO_CAPACITY-cargo_used(game)
        if misto>0:
            for i in range (3):
                n=random.choice("potravina","minerals","tech")
                game["cargo"]+=n
                print(n)
            return "atreroid"
        else:
            print("naklad je plny")
            return None
    elif event_id== "smooth":
        game[credits]+=15 
        print("bylo pricteno 15 kreditu")
        return "smooth"
    #         Zjisti volne misto (CARGO_CAPACITY - cargo_used(game)).
    #         Pokud volne > 0: vyber nahodne zbozi, pridej min(3, volne) kusu.
    #         Pouzij game["cargo"].get(good_id, 0) pro bezpecne pricteni.
    #         Vrat popis co se stalo (i kdyz byl naklad plny).
    # TODO: Implementuj vetev pro "smooth":
    #         Pricti 15 ke game["credits"], vrat popis.
    raise NotImplementedError


def travel(game):
    """Zobrazi menu planet, presune lod, spusti nahodnou udalost a posune den.

    Postup:
      1. Zobraz dostupne planety (vsechny krome aktualni).
      2. Nechej hrace vybrat (0 = zpet).
      3. Nastav game["location"], zvys game["day"] o 1.
      4. Zavolej generate_event() a apply_event(), vypis vysledek.
      5. Zavolej save_game(game).
      6. Pokud game["credits"] >= TARGET_CREDITS, vypis gratulaci.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    # TODO: Priprav slovnik dostupnych planet (bez aktualni lokace).
    a=enumerate (PLANETS.keys())
    print(a)
    for planet in PLANETS.keys():
        print(f"{planet}\n")
    while True:
        try :
            volba=int(volba=input("kam chces"))
            if volba<= 0 or volba >4:
                print("nemozne cislo")
                continue
            break
        except ValueError:
    
    # TODO: Vypis seznam planet a nechej hrace vybrat.
    #       Pouzij try/except ValueError pri cteni int ze vstupu.
    #       Over platnost volby (0 = zpet).
    # TODO: Proved zmenu lokace, inkrementuj den.
    
    # TODO: Vygeneruj udalost, aplikuj ji, vypis popis.
    # TODO: Uloz hru, zkontroluj vitezstvi, cekej na Enter.
    raise NotImplementedError


##############################################################
### CAST 4: Nakup a prodej
##############################################################

def buy_goods(game):
    # 1. Zkontroluj volné místo
    volne = CARGO_CAPACITY - cargo_used(game)
    if volne == 0:
        print("Náklad je plný! Nejdřív něco prodej.")
        input("Enter pro pokračování...")
        return

    # 2. Vypiš zboží s cenami
    planet = game["location"]
    ceny = PLANETS[planet]["prices"]       # slovník {"potravina": 10, ...}
    zbozi_list = list(ceny.items())        # [("potravina", 10), ("tech", 50), ...]

    print(f"\n=== Nákup – {planet} ===")
    print("0. Zpět")
    for i, (zbozi, cena) in enumerate(zbozi_list, 1):
        print(f"{i}. {zbozi:12} {cena} kreditů/ks")

    # 3. Načti volbu
    while True:
        try:
            volba = int(input("Co chceš koupit: "))
            if volba == 0:
                return
            if volba < 1 or volba > len(zbozi_list):
                print(f"Zadej 0–{len(zbozi_list)}.")
                continue
            break
        except ValueError:
            print("Zadej číslo.")

    zbozi, cena = zbozi_list[volba - 1]

    # 4. Kolik toho max. lze koupit
    max_buy = min(volne, game["credits"] // cena)
    if max_buy == 0:
        print("Nestačí kredity nebo místo v nákladu.")
        input("Enter pro pokračování...")
        return

    # 5. Načti množství
    while True:
        try:
            qty = int(input(f"Kolik kusů? (1–{max_buy}): "))
            if 0 < qty <= max_buy:
                break
            print(f"Zadej 1–{max_buy}.")
        except ValueError:
            print("Zadej číslo.")

    # 6. Proveď nákup
    game["credits"] -= qty * cena
    game["cargo"][zbozi] = game["cargo"].get(zbozi, 0) + qty
    save_game(game)
    print(f"✅ Koupil jsi {qty}× {zbozi} za {qty * cena} kreditů.")
    input("Enter pro pokračování...")


def sell_goods(game):
    # 1. Zkontroluj neprázdný náklad
    if not game["cargo"]:
        print("Náklad je prázdný, nemáš co prodávat.")
        input("Enter pro pokračování...")
        return

    # 2. Vypiš obsah nákladu s cenami
    planet = game["location"]
    ceny = PLANETS[planet]["prices"]
    cargo_list = list(game["cargo"].items())   # [("tech", 3), ...]

    print(f"\n=== Prodej – {planet} ===")
    print("0. Zpět")
    for i, (zbozi, pocet) in enumerate(cargo_list, 1):
        cena = ceny.get(zbozi, 0)
        zisk = pocet * cena
        print(f"{i}. {zbozi:12} {pocet} ks  →  {cena} kr/ks  (celkem {zisk} kr)")

    # 3. Načti volbu
    while True:
        try:
            volba = int(input("Co chceš prodat: "))
            if volba == 0:
                return
            if volba < 1 or volba > len(cargo_list):
                print(f"Zadej 0–{len(cargo_list)}.")
                continue
            break
        except ValueError:
            print("Zadej číslo.")

    zbozi, available = cargo_list[volba - 1]
    cena = ceny.get(zbozi, 0)

    # 4. Načti množství
    while True:
        try:
            qty = int(input(f"Kolik kusů? (1–{available}): "))
            if 0 < qty <= available:
                break
            print(f"Zadej 1–{available}.")
        except ValueError:
            print("Zadej číslo.")

    # 5. Proveď prodej
    earned = qty * cena
    game["cargo"][zbozi] -= qty
    if game["cargo"][zbozi] == 0:
        del game["cargo"][zbozi]      # ← smaž klíč pokud je 0 kusů
    game["credits"] += earned
    save_game(game)
    print(f"✅ Prodal jsi {qty}× {zbozi} za {earned} kreditů.")
    input("Enter pro pokračování...")


def clear():
    # "nt" = Windows, cokoliv jiného = Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


def print_status(game):
    clear()
    planet = game["location"]
    ceny = PLANETS[planet]["prices"]

    print("=" * 40)
    print(f"  Den: {game['day']}  |  Kredity: {game['credits']} / {TARGET_CREDITS}")
    print(f"  Planeta: {planet}")
    print("=" * 40)

    # Náklad
    print("\n📦 Náklad:")
    if game["cargo"]:
        for zbozi, pocet in game["cargo"].items():
            print(f"  {zbozi:12} {pocet} ks")
    else:
        print("  (prázdný)")

    # Ceny na planetě
    print(f"\n💰 Ceny na {planet}:")
    for zbozi, cena in ceny.items():
        print(f"  {zbozi:12} {cena} kr/ks")
    print()


def main():
    game = load_game()

    while True:
        print_status(game)
        print("1. Cestovat")
        print("2. Koupit zboží")
        print("3. Prodat zboží")
        print("4. Konec")

        volba = input("\nTvoje volba: ").strip()

        if volba == "1":
            travel(game)
        elif volba == "2":
            buy_goods(game)
        elif volba == "3":
            sell_goods(game)
        elif volba == "4":
            print("Ukončuji hru. Na shledanou!")
            break
        else:
            print("Neplatná volba.")
            input("Enter pro pokračování...")

if __name__ == "__main__":
    main()