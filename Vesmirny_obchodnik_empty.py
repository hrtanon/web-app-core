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
        with open (SAVE_FILE, "r" ) as f:
            
    # TODO: Pouzij os.path.exists() pro kontrolu existence souboru.
    # TODO: Pokud soubor existuje, otevri ho, nacti JSON a vrat slovnik.
    # TODO: Pokud neexistuje, vrat new_game().
    else :
        return new_game()
    raise NotImplementedError


def save_game(game):
    """Ulozi game slovnik do souboru SAVE_FILE ve formatu JSON.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
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
    sum()
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
    print(EVENTS["pirates":["problerm"]])
    loss= min(PIRATE_LOSS,game["credicts"])
    game["credits"]=game["credits"]-PIRATE_LOSS
    
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
    """Zobrazi menu pro nakup zbozi na aktualni planet.

    Overuje: dostupne misto v nakladu, platnost volby, dostatek kreditu.
    Po nakupu odecte kredity, prida zbozi do cargo a ulozi hru.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    # TODO: Zjisti volne misto (CARGO_CAPACITY - cargo_used(game)).
    #       Pokud je 0, vypis chybu a vrat se.
    # TODO: Vypis seznam zbozi s cenami a nechej hrace vybrat.
    #       Pouzij try/except ValueError, over platnost volby (0 = zpet).
    # TODO: Vypocti max_buy = min(volne_misto, game["credits"] // cena).
    #       Pokud je 0, vypis chybu a vrat se.
    # TODO: Nechej hrace zadat mnozstvi. Over ze 0 < qty <= max_buy.
    # TODO: Odecti kredity, pricti zbozi do game["cargo"] (pouzij .get()).
    #       Zavolej save_game(game) a vypis potvrzeni.
    raise NotImplementedError


def sell_goods(game):
    """Zobrazi menu pro prodej zbozi ze skladu za ceny aktualni planety.

    Overuje: neprazdny naklad, platnost volby, platne mnozstvi.
    Po prodeji pricte kredity, odecte zbozi z cargo (pri 0 klíc smaze) a ulozi.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    # TODO: Pokud je game["cargo"] prazdny, vypis zpravy a vrat se.
    # TODO: Priprav seznam zbozi v nakladu a vypis je s cenami a celkovym ziskem.
    # TODO: Nechej hrace vybrat zbozi (0 = zpet). Over platnost volby.
    # TODO: Nechej hrace zadat mnozstvi. Over ze 0 < qty <= available.
    # TODO: Vypocti earned = qty * cena.
    #       Odecti z cargo, pokud klesne na 0 smaz klic (del).
    #       Pricti ke kreditu, zavolej save_game(game) a vypis potvrzeni.
    raise NotImplementedError


##############################################################
### CAST 5: Zobrazeni
##############################################################

def clear():
    """Vycisti terminal (funguje na Windows i Linux/Mac)."""
    # TODO: Pouzij os.system() – na Windows prikaz "cls", jinde "clear".
    #       Tip: os.name == "nt" vraci True na Windows.
    raise NotImplementedError


def print_status(game):
    """Vycisti terminal a vypise aktualni stav hry.

    Zobrazi: den, kredity, cil, planetu, obsah nakladu, ceny na planet.

    Args:
        game: Slovnik s aktualnim stavem hry.
    """
    # TODO: Zavolej clear().
    # TODO: Vypis hlavicku s game["day"], game["credits"], TARGET_CREDITS
    #       a nazvem aktualni planety.
    # TODO: Vypis obsah game["cargo"] s nazvem zbozi a poctem kusu.
    #       Pokud je prazdny, vypis "(prazdny)".
    # TODO: Vypis ceny vsech zbozi na aktualni planet.
    raise NotImplementedError


##############################################################
### CAST 6: Hlavni smycka
##############################################################

def main():
    """Hlavni smycka hry – nacte hru, opakuje: zobraz -> menu -> akce."""
    # TODO: Zavolej load_game() a uloz vysledek do game.
    # TODO: Spust nekonecnou smycku while True.
    #         - Zavolej print_status(game).
    #         - Vypis menu s moznostmi 1-4.
    #         - Precti volbu hrace pres input().
    #         - Podle volby zavolej prislusnou funkci nebo ukonci hru (break).
    #         - Pro neplatnou volbu vypis chybu a cekej na Enter.
    raise NotImplementedError


if __name__ == "__main__":
    # PRO TESTOVANI: Odkomentuj postupne po implementaci jednotlivych casti.
    # game = new_game()
    # print(game)
    # print(cargo_used(game))
    # print(generate_event())
    # print_status(game)
    main()
