import os

def zisk_zadani():
    """
    ukol funkce otevre slozku pokud existuje a nacte otazky
    pokud neexistuje konicprogream
    """    
    try:
        with open("zadani.txt", "r", encoding="utf-8") as file:
            text=file.read()
            radky=text.splitlines()
            for n in range()
                print(radky[i])
            
        
    except FileNotFoundError:
        print("slozka s otazkami neexistuje")
        
        
zisk_zadani()