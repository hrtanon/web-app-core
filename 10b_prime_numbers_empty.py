# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram

"""Lekce 10: Prvočísla a jednoduché algoritmy v Pythonu (pracovní verze).

V tomto modulu budete krok za krokem implementovat různé algoritmy
pro testování prvočíselnosti a generování prvočísel:

ČÁST 1: Zbytek po dělení a základní test dělitelnosti
ČÁST 2: Triviální test prvočíselnosti
ČÁST 3: Generování prvočísel – jednoduchý přístup
ČÁST 4: Efektivnější test – dělení pouze do √n
ČÁST 5: Eratosthenovo síto
ČÁST 6: Porovnání výkonu algoritmů
ČÁST 7 (bonus): Prvočíselný rozklad a aplikace
ÚKOLY K PROCVIČENÍ: Další funkce na práci s prvočísly

Co se naučíte:
- použít zbytek po dělení pro test dělitelnosti,
- naivně i efektivněji testovat, zda je číslo prvočíslo,
- generovat všechna prvočísla do dané meze různými algoritmy,
- prakticky porovnat výkon odlišných implementací,
- rozložit číslo na prvočinitele a vidět souvislost s kryptografií,
- navrhnout vlastní pomocné funkce nad již napsanými algoritmy.
"""

from __future__ import annotations

import math
import time
from typing import List


##############################################################
### ČÁST 1: Zbytek po dělení a základní test dělitelnosti
##############################################################


def is_divisible(dividend: int, divisor: int) -> bool:
    """Zkontroluje, zda je jedno celé číslo dělitelné druhým.

    Pomocná funkce obalující operátor modulo. Přidává ochranu před
    dělením nulou. Bude znovu použita v dalších funkcích implementujících
    testy prvočíselnosti.

    Args:
        dividend: Dělenec (číslo, které chceme dělit).
        divisor: Dělitel (nesmí být nula).

    Returns:
        True, pokud je dividend dělitelný divisorem (zbytek je nula),
        jinak False.

    Raises:
        ValueError: Pokud je divisor roven nule.

    Příklad:
        >>> is_divisible(10, 2)
        True
        >>> is_divisible(10, 3)
        False
    """
    # TODO: Zkontrolujte, zda je divisor roven nule, a v takovém případě
    #       vyhoďte výjimku ValueError s rozumným popisem.
    if divisor<=0:
        print("nechce se mu")
    return dividend % divisor == 0
    # TODO: Pokud není divisor nulový, vraťte výsledek porovnání zbytku
    #       po dělení dividend % divisor s hodnotou 0.
    # Nápověda: Vyzkoušejte si v interaktivní konzoli, jak funguje operátor %.
    pass


##############################################################
### ČÁST 2: Triviální test prvočíselnosti
##############################################################


def is_prime_naive(n: int) -> bool:
    """Zjistí, zda je číslo prvočíslo, pomocí naivního algoritmu.

    Funkce zkouší dělitelnost všemi celými čísly od 2 do n-1.
    Je záměrně jednoduchá a pro větší n pomalá – slouží jako
    výchozí bod pro srovnání s pokročilejšími algoritmy.

    Args:
        n: Celé číslo, které chceme otestovat.

    Returns:
        True, pokud je n prvočíslo, jinak False.

    Příklad:
        >>> is_prime_naive(2)
        True
        >>> is_prime_naive(15)
        False
        >>> is_prime_naive(17)
        True
    """
    # TODO: Ošetřete hraniční případy n <= 1 (záporná čísla, 0, 1).
    if n<=1:
        return False
    elif n==2:
        return True
    for d in range(2,n-1):
        if n%d==0:
            return False
    return True
    # TODO: Ošetřete speciální případ n == 2 (jediné sudé prvočíslo).
    # TODO: Pomocí for cyklu projděte všechna čísla od 2 do n-1 a
    #       využijte funkci is_divisible k testu dělitelnosti.
    # TODO: Pokud najdete dělitele, vraťte False, jinak po skončení cyklu True.
    pass


##############################################################
### ČÁST 3: Generování prvočísel – jednoduchý přístup
##############################################################


def generate_primes_naive(limit: int) -> List[int]:
    """Vygeneruje seznam prvočísel do zadané meze (včetně).

    Implementace používá naivní test prvočíselnosti `is_prime_naive`
    pro každé číslo od 2 do limitu. Je snadno srozumitelná, ale
    pro větší limity se stává pomalou.

    Args:
        limit: Horní mez (včetně) pro generování prvočísel. Musí být >= 2,
            aby výsledek obsahoval alespoň jedno prvočíslo.

    Returns:
        Seznam prvočísel do zadané meze.

    Příklad:
        >>> generate_primes_naive(10)
        [2, 3, 5, 7]
    """
    primes=[]
    # TODO: Pokud je limit menší než 2, vraťte prázdný seznam.
    if limit<=2:
        primes=[]
    for i in range(2,limit+1):
        if is_prime_naive(i):
            primes.append(i)
    return primes

    # TODO: Vytvořte prázdný seznam pro ukládání nalezených prvočísel.
    # TODO: Pomocí for cyklu projděte všechna čísla od 2 do limitu včetně.
    # TODO: Pro každé číslo zavolejte is_prime_naive a případně jej přidejte
    #       do seznamu prvočísel.
    # TODO: Na konci vraťte seznam prvočísel.
    pass


##############################################################
### ČÁST 4: Efektivnější test – dělení pouze do √n
##############################################################


def is_prime_sqrt(n: int) -> bool:
    """Zjistí, zda je číslo prvočíslo, dělením pouze do druhé odmocniny z n.

    Tato funkce zlepšuje naivní přístup tím, že testuje potenciální dělitele
    pouze do floor(sqrt(n)) včetně. Každý netriviální dělitel větší než sqrt(n)
    by totiž musel být spárován s menším dělitelem, který bychom již dříve
    našli.

    Args:
        n: Celé číslo, které chceme otestovat.

    Returns:
        True, pokud je n prvočíslo, jinak False.

    Příklad:
        >>> is_prime_sqrt(2)
        True
        >>> is_prime_sqrt(15)
        False
        >>> is_prime_sqrt(17)
        True
    """
    if n<=1:
        return False
    elif n==2:
        return True
    if n%2==0:
        return False
    max_div=int(math.isqrt(n))
    for i in range(3,max_div,2):
        if n%i==0:
            return False
    return True
    # TODO: Stejně jako v is_prime_naive ošetřete případy n <= 1 a n == 2.
    # TODO: Rychle odmítněte všechna sudá čísla větší než 2 (nemohou být
    #       prvočísla).
    # TODO: Spočítejte horní mez pro dělení pomocí math.isqrt(n).
    # TODO: Pomocí for cyklu projděte pouze liché dělitele od 3 do
    #       vypočtené meze a hledejte dělitele.
    # Nápověda: Pro průchod jen lichými čísly použijte krok 2 v range().
    pass


##############################################################
### ČÁST 5: Eratosthenovo síto
##############################################################


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Vygeneruje prvočísla do dané meze pomocí Eratosthenova síta.

    Eratosthenovo síto je klasický algoritmus pro nalezení všech prvočísel
    do zadané meze. Postupně označuje násobky každého prvočísla počínaje 2
    jako složená; čísla, která zůstanou neoznačena, jsou prvočísla.

    Args:
        limit: Horní mez (včetně) pro generování prvočísel.

    Returns:
        Seznam prvočísel do zadané meze.

    Příklad:
        >>> sieve_of_eratosthenes(10)
        [2, 3, 5, 7]
    """
    if limit<2:
        return []
    flags= [True]*(limit+1)
    flags[0]=flags[1]=False
    hranice=int(math.sqrt(limit)+1)
    for i in range(2,hranice):
        if flags[i]:
            for multiple in range(i*i, limit + 1,i):
                flags[multiple]=False
    return [number for number, is_prime in enumerate(flags) if is_prime] 
    # TODO: Pokud je limit menší než 2, vraťte prázdný seznam.
    # TODO: Vytvořte seznam logických hodnot (True) délky limit + 1.
    # TODO: Nastavte indexy 0 a 1 na False (nejsou prvočísla).
    # TODO: Spočítejte horní mez pro hledání násobků pomocí math.isqrt(limit).
    # TODO: Pro každý number od 2 do této meze:
    #       - pokud je na daném indexu hodnota True,
    #         "vyškrtněte" všechny jeho násobky (nastavte na False),
    #         počínaje číslem number * number.
    # TODO: Na závěr převeďte seznam True/False na seznam indexů, které
    #       zůstaly True (to jsou prvočísla).
    primes_naive = generate_primes_naive(limit)
    primes_sieve = sieve_of_eratosthenes(limit)
    # Nápověda: Využijte enumerate() pro převod seznamu příznaků na čísla.
    pass


##############################################################
### ČÁST 6: Porovnání výkonu algoritmů
##############################################################


def benchmark_prime_algorithms(limit: int) -> None:
    """Porovná rychlost různých algoritmů pro generování prvočísel.

    Funkce měří dobu běhu:
    - naivního generátoru prvočísel `generate_primes_naive` a
    - Eratosthenova síta `sieve_of_eratosthenes`.

    Vytiskne dobu běhu každého přístupu v sekundách a ověří, zda oba
    algoritmy vrátily stejný seznam prvočísel.

    Args:
        limit: Horní mez (včetně) pro generování prvočísel v benchmarku.

    Returns:
        None. Výsledky se vypíší na standardní výstup.

    Příklad:
        >>> benchmark_prime_algorithms(1000)
        === Benchmark for limit = 1000 ===
        ...
    """
    start=time.perf_counter()
    generate_primes_naive(limit)
    cas1=time.perf_counter()-start
    print(f"{cas1:.6f} s")
    # TODO: Vytiskněte úvodní hlavičku benchmarku (oddělovače + limit).
    # TODO: Změřte čas pro generate_primes_naive pomocí time.perf_counter()
    start=time.perf_counter()
    sieve_of_eratosthenes(limit)
    cas=time.perf_counter()-start
    print(f"{cas:.6f} s")
    primes_naive = generate_primes_naive(limit)
    primes_sieve = sieve_of_eratosthenes(limit)
    if primes_sieve==primes_naive:
        print ("sedi")
    else:
        print("NESEDI")
    # TODO: Změřte čas pro sieve_of_eratosthenes stejným způsobem.
    # TODO: Vytiskněte do konzole dobu běhu obou algoritmů ve vteřinách
    #       s rozumným formátováním.
    # TODO: Porovnejte, zda oba algoritmy vrátily stejný seznam prvočísel
    #       a výsledek (True/False) vytiskněte.
    # Nápověda: Použijte f-stringy a zaokrouhlete čas na 6 desetinných míst.
    pass


##############################################################
### ČÁST 7 (bonus): Prvočíselný rozklad a aplikace
##############################################################


def prime_factorization(n: int) -> List[int]:
    """Rozloží kladné celé číslo na prvočinitele.

    Rozklad je vrácen jako seznam prvočinitelů v neklesajícím pořadí.
    Například 12 → [2, 2, 3]. Algoritmus je jednoduchý, ale účinný
    pro středně velká celá čísla; využívá myšlenku zkušebního dělení
    do druhé odmocniny z n.

    Args:
        n: Kladné celé číslo k rozložení.

    Returns:
        Seznam prvočinitelů v neklesajícím pořadí. Pro n <= 1 vrátí
        prázdný seznam.

    Raises:
        ValueError: Pokud je n záporné.

    Příklad:
        >>> prime_factorization(1)
        []
        >>> prime_factorization(12)
        [2, 2, 3]
        >>> prime_factorization(13)
        [13]
    """
    # TODO: Pokud je n záporné, vyhoďte ValueError (záporná čísla zde
    #       nerozkládáme).
    # TODO: Pokud je n <= 1, vraťte prázdný seznam (žádní prvočinitelé).
    # TODO: Vytvořte prázdný seznam factors pro ukládání prvočinitelů.
    # TODO: Nejprve opakovaně dělte n číslem 2, dokud je dělitelné,
    #       a vždy přidejte 2 do seznamu factors.
    # TODO: Poté hledejte liché dělitele od 3 výše, dokud divisor * divisor
    #       není větší než n, a obdobně je přidávejte do factors.
    # TODO: Pokud po dělení zůstane n > 1, přidejte toto n jako poslední
    #       prvočinitel.
    # Nápověda: V této funkci stačí používat operátory %, // a jednoduché cykly.
    pass


##############################################################
### ÚKOLY K PROCVIČENÍ (bonusové návrhy)
##############################################################


def count_primes_in_interval(start: int, end: int) -> int:
    """Spočítá, kolik prvočísel leží v zadaném uzavřeném intervalu.

    Navrhovaný postup:
    - Znovu použijte jeden z výše implementovaných testů prvočíselnosti.
    - Zamyslete se nad ošetřením vstupu (co když start > end?).

    Args:
        start: Začátek intervalu (včetně).
        end: Konec intervalu (včetně).

    Returns:
        Počet prvočísel v intervalu.

    """
    # TODO: Ošetřete případ, kdy start > end (např. prohozením hodnot).
    # TODO: Inicializujte čítač počtu prvočísel na nulu.
    # TODO: Pomocí vhodného primality testu (např. is_prime_sqrt) spočítejte,
    #       kolik čísel v intervalu [start, end] je prvočísel.
    pass


def largest_prime_below(limit: int) -> int | None:
    """Najde největší prvočíslo menší nebo rovno zadané mezi.

    Navrhovaný postup:
    - Procházejte čísla od limitu směrem dolů a vraťte první prvočíslo.
    - Zvažte, co má funkce vrátit pro limit < 2.

    Args:
        limit: Horní mez prohledávání.

    Returns:
        Největší prvočíslo <= limit, nebo None, pokud takové neexistuje.

    """
    # TODO: Pokud je limit menší než 2, vraťte None (žádné prvočíslo).
    # TODO: Procházejte čísla od limit směrem dolů k 2 a použijte
    #       is_prime_sqrt pro test prvočíselnosti.
    # TODO: Jakmile najdete prvočíslo, ihned jej vraťte.
    # TODO: Pokud cyklus skončí bez nálezu, vraťte None.
    pass


def primes_with_fixed_digit_count(num_digits: int) -> List[int]:
    """Vygeneruje všechna prvočísla s přesně zadaným počtem číslic.

    Navrhovaný postup:
    - Spočítejte interval [10^(d-1), 10^d - 1] a hledejte prvočísla v něm.
    - Diskutujte výkon pro větší počty číslic.

    Args:
        num_digits: Počet desetinných číslic (musí být >= 1).

    Returns:
        Seznam prvočísel, která mají právě num_digits číslic.

    """
    # TODO: Pokud je num_digits menší než 1, vraťte prázdný seznam.
    # TODO: Spočítejte dolní mez intervalu (10 ** (num_digits - 1)).
    # TODO: Spočítejte horní mez intervalu (10 ** num_digits - 1).
    # TODO: Pro všechna čísla v tomto intervalu otestujte, zda jsou prvočísla
    #       (např. pomocí is_prime_sqrt) a průběžně je ukládejte do seznamu.
    # TODO: Vraťte seznam nalezených prvočísel.
    pass


##############################################################
### DEMONSTRAČNÍ MAIN BLOK
##############################################################



    """Spustí základní ukázku implementované funkcionality.

    Funkce slouží k rychlému vizuálnímu přehledu toho, jak se různé
    algoritmy chovají a jak vypadají jejich výstupy.
    """
    # TODO: Zvolte malý limit (např. 30) a vytiskněte seznam prvočísel
    #       získaných pomocí generate_primes_naive a sieve_of_eratosthenes.
    # TODO: Připravte několik čísel a porovnejte výsledek is_prime_naive
    #       a is_prime_sqrt pro stejná n.
    # TODO: Vytiskněte několik příkladů prvočíselného rozkladu pomocí
    #       prime_factorization.
    # Nápověda: Dbejte na přehledné oddělovače a popisky, aby byl výstup
    #           srozumitelný i bez nahlížení do kódu.
def _demo_basic() -> None:
    """Spustí základní ukázku implementované funkcionality (bez bonusů)."""
    limit = 30
    print("=== Demo: Generování prvočísel do", limit, "===")
    
    # Naivní generátor
    primes_naive = generate_primes_naive(limit)
    print("Naivní generátor:", primes_naive)
    
    # Eratosthenovo síto
    primes_sieve = sieve_of_eratosthenes(limit)
    print("Eratosthenovo síto:", primes_sieve)
    
    # Porovnání shody
    print("Seznamy shodné:", primes_naive == primes_sieve)
    
    # Test prvočíselnosti
    test_numbers = [1, 2, 3, 4, 17, 20, 29]
    print("\n=== Test prvočíselnosti ===")
    for n in test_numbers:
        print(f"{n}: Naivní test = {is_prime_naive(n)}, Test do √n = {is_prime_sqrt(n)}")


if __name__ == "__main__":
    _demo_basic()