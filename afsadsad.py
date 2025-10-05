import math
import os
import matplotlib.pyplot as plt 
os.system("cls")


# ňesmim dat do parametnu urcuite veci kdyz pak chci aby byli dany az inputem

def strany_trojuhelniku():
    """

    vyzada stranu kterou zadate pak je vraci jako a,b,c pokud lze trojuhelnik sestrojit 
    return:
    kvuli tomu podminka if  a trouhelnikova nerovnost
    """
    while True:
     try:
        a = float(input("Jaká je první strana? "))
        b = float(input("Jaká je druhá strana? "))
        c = float(input("Jaká je třetí strana? "))
        if a==0  or b==0  or c==0 :
            print(f"nula zatat preci nemuezs")
            continue
        
      
     except ValueError:
        print("Chyba! Zadej prosím číslo.")
        continue
     if  a<=0 or b<=0 or c<=0 :
        print("zadej platne cisla")
        continue
         

     if a+b<=c or a+c<=b or c+b<=a:
         print(f"nelze sestrojit trojuhelnik s techle stran")
         continue
    
     return a,b,c
def uhly_trojuhelniku(a,b,c):
    alfa = math.degrees(math.acos((b**2 + c **2 - a**2)/ (2*b*c)))
    bravo = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    charlie = math.degrees(math.acos((b**2+a**2-c**2)/(2*a*b)))
    return alfa, bravo , charlie

def obvod_a_obsah(a,b,c):
   obvod=a+b+c
   s=(a+b+c)/2
   obsah=(s*(s-a)*(s-b)*(s-c))**0.5
   return obvod, obsah

def kruh_vepsana_a_opsana(a,b,c,obsah):
    S=obsah
    ops= (a+b+c)/(4 * S )
    vesp= S/ ((a+b+c)/2)
    print(f"polomer kruznice opsane  je: {ops:.2f}")
    print(f"polomer kruznice vepsane  je: {vesp:.2f}")
    return vesp, ops
    


trojuhelnik = strany_trojuhelniku() 
a , b, c = trojuhelnik
uhly = uhly_trojuhelniku(a, b, c)
obvod,obsah =obvod_a_obsah(a, b, c)
print(f"Strany trojúhelníku: a={a:.2f}, b={b:.2f}, c={c:.2f}")
print(f"Úhly trojúhelníku (stupně): alfa={uhly[0]:.2f}, bravo={uhly[1]:.2f}, charlie={uhly[2]:.2f}")
print(f"Obvod: {obvod:.2f}, Obsah: {obsah:.2f}")

kruh_vepsana_a_opsana(a,b,c,obsah)



def vykres(a,b,c):
   cos_charlie = (a**2+b**2-c**2)/(2*a*b)
   charlie=math.acos(cos_charlie)
   x1,y1=0,0
   x2,y2=a,0
   x3=b*math.cos(charlie)
   y3=b*math.sin(charlie)
   plt.plot([x1,x2,x3],[y1,y2,y3])
   plt.fill([x1,x2,x3],[y1,y2,y3],"r")
   plt.gca().set_aspect("equal", adjustable="box")
   plt.title("trojka")
   plt.show()
vykres(a,b,c)
