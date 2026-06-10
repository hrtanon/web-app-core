import random
import os
from abc import ABC, abstractmethod



class Charakters:
    
    def __init__(self,jmeno,hp,mana,level):
        self.jmeno=jmeno
        self.level=level
        self.mana=mana
        self.hp=hp
        self.inventory = []
    def armor(self,damage):
        
        self.hp-=damage-self.level
        return self.hp
    def levelup(self):
        self.level += 1
        

    def __add__(self, other):
        
        if isinstance(other, Charakters):
            combined_inventory = self.inventory + other.inventory
            return combined_inventory
        raise ValueError("Lze kombinovat pouze inventáře postav.")
    def __str__(self):
        return f"{self.hp} hp , {self.level}level , {self.jmeno} ma {self.mana} many"  


class Bruisers(Charakters):
    
    def __init__(self, jmeno, hp, mana, level):
        super().__init__(jmeno, hp, mana, level)
    def atttac(self,base_damage,power):
        damage=base_damage+self.level*power
        return damage
    



class mage(Charakters):
    def __init__(self, jmeno, hp, mana, level):
        super().__init__(jmeno, hp, mana, level)
    def insteligence(self):
        
        inteligence=self.level*0.35
        return inteligence
    def atttac(self,base_damage):
        damage=self.insteligence()*base_damage+10
        cost=40
        if self.mana >= cost:
            self.mana -= cost
        else:
            print("Nedostatek many")
        
        
        return damage


def power_boost(func):
    def wrapper(*args,**kwargs):
        base_damage=func(*args,**kwargs)
        boosted_dam=base_damage+10
        print("Síla útoku byla zvýšena o 10 bodů!")
        return boosted_dam
    return wrapper
    
ryze=Charakters("ryze",1,50,350)
ryze.__str__()

print(ryze)




class PlayableCHarakters(ABC):
    @abstractmethod
    def levelup(self):
        pass
    @abstractmethod
    def atttac(self,base_damage):
        pass
    @abstractmethod
    def armor(self):
        pass
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        """Nastavení zdraví s kontrolou nula až max."""
        if value > self.MAX_HEALTH:
            self._health = self.MAX_HEALTH
        elif value < 0:
            self._health = 0  # Zdraví nesmí být záporné
        else:
            self._health = value



def Generate_random_charakters()-> Charakters:
    characters = []

    for _ in range(3):
        pohlavi=random.choice(["x"],["y"])
        if pohlavi =="x":
            characters.append(Bruisers("Thor", 100, 20, 1))
        elif pohlavi=="y":
            characters.append(mage("Merlin", 80, 50, 1))
    return characters
    