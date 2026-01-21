# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""Hashování hesel v Pythonu

Tento pracovní soubor vás provede vytvořením bezpečného systému pro správu 
uživatelských hesel.

- Co je hashování a proč je důležité
- Jak použít knihovnu hashlib v Pythonu
- Jak vytvořit registrační a přihlašovací systém
- Jak validovat uživatelské vstupy

Při práci používejte studijní text jako oporu, ale snažte se nejprve přijít 
na řešení sami. Každá část obsahuje komentáře s nápovědou.
"""

import os
import hashlib
# Pro pokročilejší část budete potřebovat regulární výrazy
import re


##############################################################
### ČÁST 1: Základní hashování hesla
##############################################################

# Hashování je jednosměrný proces - z hashe nemůžeme získat původní heslo zpět
# Použijeme algoritmus SHA-256 z knihovny hashlib

def hash_password(heslovina):
    """Vytvoří SHA-256 hash zadaného hesla.
    
    Funkce převede heslo na bytes a následně pomocí SHA-256 vytvoří hash.
    Výsledek vrátí jako hexadecimální řetězec (64 znaků).
    
    Args:
        password: Heslo v textové podobě, které chceme zhashovat
        
    Returns:
        Hexadecimální řetězec reprezentující hash hesla
        
    Příklad:
        >>> hash_password("mojeHeslo123")
        'a1b2c3d4...' (64 znaků)
    """
    # TODO: Převeďte heslo na bytes pomocí metody .encode('utf-8')
    heslovina_bytes= heslovina.encode("utf-8")
    hash_code=hashlib.sha256(heslovina_bytes)
    hex_heslovina= hash_code.hexdigest()
    print(hex_heslovina)
    # TODO: Vytvořte hash pomocí hashlib.sha256()
    # TODO: Vraťte hexadecimální reprezentaci pomocí .hexdigest()
    return hex_heslovina


# TESTOVÁNÍ: Po implementaci funkce odkomentujte a vyzkoušejte:
# print("Test hashování:")
# print(hash_password("testHeslo123"))
# print(hash_password("testHeslo123"))  # Měl by být stejný
# print(hash_password("testHeslo124"))  # Měl by být jiný


##############################################################
### ČÁST 2: Kontrola existence uživatele
##############################################################

# Před registrací nového uživatele musíme zkontrolovat, zda už neexistuje
# Projdeme soubor users.txt a hledáme zadaný e-mail

def user_exists(email):
    """Zkontroluje, zda uživatel s daným e-mailem již existuje v systému.
    
    Funkce otevře soubor users.txt a prohledá jej po řádcích. Každý řádek
    obsahuje e-mail a hash oddělené čárkou. Pokud najde shodu s e-mailem,
    vrátí True.
    
    Args:
        email: E-mailová adresa k ověření
        
    Returns:
        True pokud uživatel existuje, False pokud neexistuje nebo soubor 
        neexistuje
    """
    # TODO: Použijte try-except pro ošetření FileNotFoundError
    try :
        with open("emaly.txt", "r", encoding="utf-8") as file:
            for line in file:
                ulozene_maly,_ =line.strip().split(",")
                if email== ulozene_maly:
                    print("more maily tam uz mame")
                    return True
        return False
    
    except FileNotFoundError:
        return False
    
    # TODO: Otevřete soubor "users.txt" v režimu čtení ("r") s kódováním utf-8
    # TODO: Projděte soubor po řádcích
    # TODO: Každý řádek rozdělte pomocí .strip().split(',')
    # TODO: Porovnejte e-mail ze souboru se zadaným e-mailem
    # TODO: Pokud se shodují, vraťte True
    # TODO: Pokud projdete celý soubor bez shody, vraťte False
    # TODO: V except bloku vraťte False (soubor neexistuje = žádní uživatelé)
    pass


##############################################################
### ČÁST 3: Registrace nového uživatele
##############################################################

# Při registraci uložíme e-mail a HASH hesla do souboru
# NIKDY neukládáme původní heslo!

def register_user(email, password):
    """Zaregistruje nového uživatele do systému.
    
    Funkce nejprve zkontroluje, zda uživatel již neexistuje. Pokud neexistuje,
    zhashuje jeho heslo a uloží e-mail spolu s hashem do souboru users.txt.
    Každý uživatel je na vlastním řádku ve formátu: email,hash
    
    Args:
        email: E-mailová adresa nového uživatele
        password: Heslo v původní podobě (bude zhashováno)
        
    Returns:
        True pokud registrace proběhla úspěšně, False pokud uživatel 
        již existuje
    """
    if user_exists(email)==False:
        with open("emaly.txt", "a", encoding="utf-8")as file:
            file.write(f"{email},{hash_password(password)}\n")
            print(f"registrace probehla more")
        return True
    
    
    return False
    # TODO: Zkontrolujte pomocí user_exists(), zda uživatel již neexistuje
    # TODO: Pokud existuje, vypište hlášku a vraťte False
    # TODO: Zhashujte heslo pomocí funkce hash_password()
    # TODO: Otevřete soubor "users.txt" v režimu připojování ("a") s utf-8
    # TODO: Zapište do souboru řádek ve formátu: f"{email},{hash}\n"
    # TODO: Vypište úspěšnou hlášku a vraťte True
    


##############################################################
### ČÁST 4: Přihlášení uživatele
##############################################################

# Přihlášení funguje tak, že zhashujeme zadané heslo a porovnáme
# tento hash s hashem uloženým v souboru

def login_user(email, password):
    """Pokusí se přihlásit uživatele do systému.
    
    Funkce zhashuje zadané heslo a porovná výsledný hash s hashem uloženým
    v souboru users.txt pro daný e-mail. Pokud se hashe shodují, přihlášení
    je úspěšné.
    
    Args:
        email: E-mailová adresa uživatele
        password: Heslo zadané při přihlášení
        
    Returns:
        True pokud přihlášení bylo úspěšné (správný e-mail i heslo),
        False pokud přihlášení selhalo nebo uživatel neexistuje
    """
    hash=hash_password(password)
    try:
        with open("emaly.txt", "r",encoding="utf-8") as file:
            for line in file:
                line=line.strip()
                if not line:
                    continue
                email_ulozeny, uloz_hash= line.strip(",")
                if email==email_ulozeny:
                    if hash==uloz_hash:
                        print("uspesne prihlaseni")
                        break
                    elif hash==None:
                        print("heslo jeste nemate")
                        break
                    else:
                        print("heslo se neshoduje ")
                else:
                    print("nebyl jste prihlasen")
                    with open("emaly.txt", "a", encoding="utf-8")as file:
                        file.write(f"{email},{hash_password(password)}/n")
                        print(f"registrace probehla more")
                        break
    except FileNotFoundError:
        print("jeste neexistuje vas ucet nebo slozka kde by mel byt prihlasim vas")
        with open("emaly.txt", "a", encoding="utf-8")as file:
                        file.write(f"{email},{hash_password(password)}/n")
                        print(f"registrace probehla more")
        return
    # TODO: Zhashujte zadané heslo pomocí hash_password()
    # TODO: Použijte try-except pro ošetření FileNotFoundError
    # TODO: Otevřete soubor "users.txt" v režimu čtení s utf-8
    # TODO: Projděte soubor po řádcích
    # TODO: Přeskočte prázdné řádky (pokud line.strip() je prázdné)
    # TODO: Rozdělte řádek na e-mail a hash pomocí .split(',')
    # TODO: Pokud se e-mail shoduje se zadaným:
    #       - Porovnejte zhashované heslo s hashem ze souboru
    #       - Pokud se shodují, vypište úspěch a vraťte True
    #       - Pokud ne, vypište "Nesprávné heslo" a vraťte False
    # TODO: Pokud e-mail nebyl nalezen, vypište hlášku a vraťte False
    # TODO: V except bloku vypište hlášku o neexistujícím souboru a vraťte False
    pass


##############################################################
### ČÁST 5: Pokročilá validace (BONUSOVÁ ČÁST)
##############################################################

# Pro skutečné aplikace potřebujeme validovat vstupy uživatelů
# Zkontrolujeme formát e-mailu a sílu hesla

def validate_email(email):
    """Zkontroluje, zda e-mail má správný formát.
    
    Používá regulární výraz pro základní kontrolu formátu e-mailové adresy.
    Ověřuje přítomnost @ a tečky v doméně.
    
    Args:
        email: E-mailová adresa ke kontrole
        
    Returns:
        True pokud e-mail má platný formát, jinak False
    """
    # TODO: Použijte regulární výraz pro kontrolu formátu
    # Pattern: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # TODO: Použijte re.match() a zkontrolujte, zda výsledek není None
    pass


def validate_password(password):
    """Zkontroluje sílu hesla podle definovaných pravidel.
    
    Pravidla pro heslo:
    - Minimálně 8 znaků
    - Alespoň jedno velké písmeno
    - Alespoň jedno malé písmeno
    - Alespoň jedna číslice
    
    Args:
        password: Heslo ke kontrole
        
    Returns:
        Tuple (bool, str): První hodnota je True/False (zda heslo vyhovuje),
        druhá hodnota je zpráva s popisem problému nebo potvrzením
    """
    # TODO: Zkontrolujte délku pomocí len() - minimálně 8 znaků
    # TODO: Použijte any() a generator expression pro kontrolu velkých písmen
    #       Příklad: any(c.isupper() for c in password)
    # TODO: Podobně zkontrolujte malá písmena pomocí .islower()
    # TODO: Podobně zkontrolujte číslice pomocí .isdigit()
    # TODO: Pro každé nesplněné pravidlo vraťte (False, "popis problému")
    # TODO: Pokud vše projde, vraťte (True, "Heslo je dostatečně silné.")
    pass


def register_user_advanced(email, password, password_confirm):
    """Vylepšená registrace s kompletní validací vstupů.
    
    Tato verze kontroluje:
    - Shodu zadaných hesel
    - Platnost formátu e-mailu
    - Sílu hesla podle definovaných pravidel
    
    Args:
        email: E-mailová adresa nového uživatele
        password: Heslo pro registraci
        password_confirm: Kontrolní zadání hesla (musí se shodovat)
        
    Returns:
        True pokud registrace proběhla úspěšně, False při jakémkoliv problému
    """
    # TODO: Zkontrolujte, zda se hesla shodují
    # TODO: Zavolejte validate_email() a zkontrolujte výsledek
    # TODO: Zavolejte validate_password() a zpracujte výsledek (tuple)
    # TODO: Pokud vše projde, zavolejte původní register_user()
    pass


##############################################################
### ČÁST 6: Hlavní program s menu
##############################################################
def ziskani_hodnot():
    while True:
        try:
            moznost=int(input("zadej co chces"))
            if 0>=moznost or moznost>=4:
                print ("neplatny vstup")
                continue
            else :
                return moznost
        except ValueError:
            print("neplatny vstup")
            continue
def ziskat_emal():
    while True:
        try:
            email=input("zadej maila").strip()
            if "@" not in email:
                print("to neni mail ani za nic")
                continue
            else:
                return email
            
        except ValueError:
            print ("to neni mail zkus znova")
            continue
    
def zisk_heslo():
    while True:
        password=input("zadej si heslo \n aspon 8 znaku").strip()
        if not password:
            print("neco zadej more")
            continue
        delka=len(password)
        if delka<8:
            print("dej delsi heslo")
            continue
        else:
            return password
def main():
    """Hlavní program s interaktivním textovým menu.
    
    Nabízí uživateli tři možnosti:
    1. Registrace nového uživatele
    2. Přihlášení existujícího uživatele
    3. Ukončení programu
    """
    print("=" * 50)
    print("   SYSTÉM SPRÁVY UŽIVATELSKÝCH ÚČTŮ")
    print("=" * 50)
    print()
    for i in range(5):
        cislo=ziskani_hodnot()
        if cislo==1:
            email=ziskat_emal()
            password=zisk_heslo()
            register_user(email,password)
            print("registace probehla")
            break
        elif cislo==2:
            email=ziskat_emal()
            password=zisk_heslo()
            login_user(email,password)
            print("byli jse prihlaseni")
            break
        elif cislo==3:
            print("treba nekdy priste")
            break
    # TODO: Vytvořte nekonečnou smyčku while True
    # TODO: Vypište menu s možnostmi 1-3
    # TODO: Získejte volbu uživatele pomocí input().strip()
    
    # TODO: Pro volbu "1" - Registrace:
    #       - Získejte e-mail a heslo od uživatele
    #       - Proveďte základní kontrolu (neprázdné hodnoty, @ v e-mailu)
    #       - Zavolejte register_user() nebo register_user_advanced()
    #       - BONUSOVĚ: Pro advanced verzi získejte heslo dvakrát
    
    # TODO: Pro volbu "2" - Přihlášení:
    #       - Získejte e-mail a heslo od uživatele
    #       - Zavolejte login_user()
    
    # TODO: Pro volbu "3" - Ukončení:
    #       - Vypište rozlučkovou zprávu
    #       - Ukončete smyčku pomocí break
    
    # TODO: Pro neplatnou volbu vypište chybovou hlášku
    
    pass
main()


##############################################################
### ÚKOLY K PROCVIČENÍ (po dokončení základní verze)
##############################################################

# ÚKOL 1: Přidejte funkci, která zobrazí seznam všech registrovaných
#         e-mailů (ale ne hashe!). Může být užitečná pro administrátora.

def list_users():
    """Zobrazí seznam všech registrovaných e-mailů."""
    # TODO: Implementujte
    pass


# ÚKOL 2: Vytvořte funkci pro změnu hesla, která vyžaduje zadání
#         starého hesla před nastavením nového.

def change_password(email, old_password, new_password):
    """Změní heslo uživatele po ověření starého hesla.
    
    Args:
        email: E-mailová adresa uživatele
        old_password: Současné heslo pro ověření
        new_password: Nové heslo, které má být nastaveno
        
    Returns:
        True pokud změna proběhla úspěšně, jinak False
    """
    # TODO: Implementujte
    # Nápověda: Budete muset přečíst celý soubor, upravit příslušný
    # řádek a zapsat soubor znovu
    pass


# ÚKOL 3: Implementujte systém, který po třech neúspěšných pokusech
#         o přihlášení dočasně zablokuje účet.
#         Hint: Budete potřebovat slovník pro sledování pokusů

failed_login_attempts = {}

def login_with_protection(email, password):
    """Přihlášení s ochranou proti brute-force útokům.
    
    Args:
        email: E-mailová adresa
        password: Heslo
        
    Returns:
        True při úspěšném přihlášení, False při neúspěchu nebo blokaci
    """
    # TODO: Implementujte
    heslo ="aaaaa"

    hash_password(heslo)
    # Nápověda: Použijte globální slovník failed_login_attempts
    pass


##############################################################
### Spuštění programu - MAIN
##############################################################

if __name__ == "__main__":
    os.system("cls")
    
    # TODO: Po implementaci odkomentujte:
    # main()
    
    # PRO TESTOVÁNÍ: Můžete zde testovat jednotlivé funkce
    print("Pracovní soubor pro lekci o hashování hesel")
    print("Postupujte podle komentářů v kódu a implementujte jednotlivé funkce.")
    print()
    print("TESTOVACÍ SEKCE:")
    print("-" * 50)
    main()
    
    # Příklad testování hash funkce:
    # test_password = "testHeslo123"
   
main()