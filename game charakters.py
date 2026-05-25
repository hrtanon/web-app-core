import random
import os



class Charakters:
    def __init__(self,jmeno):
        self.jmeno=jmeno
    def __str__(self,hp):
        self.health=hp 
        return f"{self.health}"
    def __str__(self,hp):
        self.health=hp 
        return f"{self.health}"
        
ryze=Charakters("ryze")
print(ryze.jmeno)


ryze.health(40)






mel=Charakters("mel")
print(mel.jmeno)
        
mel.health=40