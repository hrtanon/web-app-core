# Zde je sada praktických úloh a cvičení na práci se soubory v Pythonu – ideální pro procvičení základních dovedností podle předchozího přehledu.
from pathlib import Path
import os
import time

# 1. Zjišťování a manipulace s cestami
""" 
- Vypiš aktuální pracovní adresář.
- Zjisti domovskou složku uživatele.
- Vytvoř podadresář "test_soubory" ve své domovské složce (použij `pathlib` i `os`).
- Sestav absolutní cestu k souboru `"example.txt"` v této nové složce.
"""
home=Path.home()
print(home)
p=home/"test_soubory"/"TEXT_SOUBOR"/"ouvej"/"monalisa.txt"
os.makedirs(p, exist_ok=True)
akt=Path.cwd()
marek=Path(p).absolute
print(marek)


# 2. Práce s jednotlivými částmi cesty
""" 
- Vytvoř nějakou cestu ke zvolenému souboru (`data.txt`) a vypiš:
  - Kořen (anchor)
  - Nadřazenou složku (parent)
  - Název souboru (name)
  - Příponu (suffix).parent   # WindowsPath('C:/Users/Al')
  p.name     # 'spam.txt'
  p.stem     # 'spam'
  p.suffix   # '.txt'
  p.parts    # ('C:\\', 'Users', 'Al', 'spam.txt')
  - Seznam všech částí cesty (`parts`)
- Spočítej, kolik rodičovských složek má aktuální pracovní adresář.
 """

print(p.anchor)   # 'C:\\'
print(p.parent )  # WindowsPath('C:/Users/Al')
print(p.name)     # 'spam.txt'
print(p.stem)     # 'spam'
print(p.suffix)   # '.txt'
print(p.parts)
print(akt.parent)

### 3. Kontrola existence a typu cesty
""" 
- Ověř, zda cesta `"test_soubory"` existuje a je složka.
- Zkus zkontrolovat neexistující složku a interpretuj výsledek.
- Zjisti, zda existuje nějaký soubor `"example.txt"`, a zda je to soubor.
 """



### 4. Vyhledávání souborů - glob
""" 
- Pomocí `glob('*')` vypiš všechny soubory a složky ve složce `"test_soubory"`.
- Vytvoř ve složce `"test_soubory"` několik souborů různých typů (např. `"a.txt"`, `"b.csv"`, `"obrazek.png"`).
- Najdi všechny textové soubory (`*.txt`) ve složce a vypiš jejich jména.
"""



### 5. Zápis a čtení textových souborů
""" 
- Vytvoř a zapiš do souboru `"test_soubory/pokus.txt"` větu dle vlastního výběru.
- Do stejného souboru při dalším spuštění přidej na konec další řádek.
- Soubor znovu načti a vypiš celý jeho obsah.
- Pomocí metody `readlines()` získej seznam všech řádků ze souboru a vypiš počet řádků.
"""



### 6. Bezpečná práce se soubory pomocí `with`
""" 
- Přepiš předchozí úlohu tak, aby otevření a zápis do souboru proběhl uvnitř konstrukce `with`.
- Ověř, že soubor je po ukončení bloku zavřený (zkus zápis mimo blok – co se stane?).
"""



### 7. Domácí úkol (volitelný)
""" 
- Vytvoř program, který zadanou složku rekurzivně projde a vypíše názvy všech souborů s příponou `.py`.
- Rozšiř: Ke každému souboru vypiš ještě datum poslední úpravy a velikost v KB.
"""


