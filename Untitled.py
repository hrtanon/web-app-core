import os
from datetime import datetime
import random

daytimes = datetime.now().hour


os.system("cls")
jmeno=input(f"jake je vase jmeno?")
prijmeni=input(f"a tve primeni?")
while jmeno =="" :
        print(f"to neni jmeno")
        input(f"jake je tve jmeno?")
        break
  
if daytimes <12 :
        print(f"dobre rano sefe")
        print(f"rad te poznavam {jmeno } ")
elif 12< daytimes <20 :
        print(f"dobrý vodpolene")
        print(f"rad te poznavam {jmeno } ")
else :
        print(f"nemas uz spat?")
        print(f"ale rad te poznavam {jmeno } ") 
pozdrav=["ahoj" , "hi", "dobry dopo"]
random.seed() 
print(random.choice(pozdrav))
os.system("cls")

   
