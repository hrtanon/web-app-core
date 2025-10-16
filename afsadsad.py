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
         

     if a+b<c or a+c<b or c+b<a:
         print(f"nelze sestrojit trojuhelnik s techle stran")
         continue
     print(f"Strany trojúhelníku: a={a:.2f}, b={b:.2f}, c={c:.2f}, tenhle trrojuhelnik sel sestrojit")
     return a,b,c


def uhly_trojuhelniku(a,b,c):
    """pocita uhly trojuhelniku pomoci cosinovy vety
    promene a,b,c z prvni funkce"""
    alfa = math.degrees(math.acos((b**2 + c **2 - a**2)/ (2*b*c)))
    bravo = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
    charlie = math.degrees(math.acos((b**2+a**2-c**2)/(2*a*b)))
    print(f"Úhly trojúhelníku (stupně): alfa={alfa:.2f}, bravo={bravo:.2f}, charlie={charlie:.2f}")
    return alfa, bravo , charlie

def obvod_a_obsah(a,b,c):
   """pocitaci obvod obsah trojuhelniku
   promene a,b,c z prvni funkce"""
   obvod=a+b+c
   s=(a+b+c)/2
   obsah=(s*(s-a)*(s-b)*(s-c))**0.5
   print(f"Obvod: {obvod:.2f}, Obsah: {obsah:.2f}")
   return obvod, obsah

def kruh_vepsana_a_opsana(a,b,c,obsah):
    """bere promene a,b,c z prvni funkce 
    z druhe obsah a pote vypocita polomery"""
    S=obsah
    ops= (a+b+c)/(4 * S )
    vesp= S/ ((a+b+c)/2)
    print(f"polomer kruznice opsane  je: {ops:.2f}")
    print(f"polomer kruznice vepsane  je: {vesp:.2f}")
    return vesp, ops

def typ_troj(a,b,c):
   """ukaze jaky typ trojuhelniku to je dle rovnosti stran"""
   if a==b==c:
      print(f"trojuhelnik je rvnostrany")
   elif a==b or a==c or b==c:
      print(f"trojuhelnik je rovnorameny")
   else:
      print(f"trojuhelnik je ruzno strany")


# ďefenice promenych do funkci






def vykres(a,b,c):
   """funkce nakresni trojuhelnik
   input jsou strany zadane u trojuhelniku
   meritko jedna ku jedne
   trojuhelnik by mel byt cerveny"""
   cos_charlie = (a**2+b**2-c**2)/(2*a*b)
   charlie=math.acos(cos_charlie)
   x1,y1=0,0
   x2,y2=a,0
   x3=b*math.cos(charlie)
   y3=b*math.sin(charlie)
   plt.plot([x1,x2,x3],[y1,y2,y3])
   plt.fill([x1,x2,x3],[y1,y2,y3],"r")
      # vyplneni a barva
   plt.gca().set_aspect("equal", adjustable="box")
      # ňastavevi jedna ku jedne
   plt.title("trojka")
   plt.show()








def lobyy():
   """inpit volby a pote ocekavane vykresleni zvolene funkce"""
   
   a,b,c=strany_trojuhelniku()
   
   
    
   print(f"co se chces dneska dozvedet\n pokud chces znat zda jde trojuhelnik sestavit a jeho typ zadej 1\npokud chces vykresleni trojuhelniku zadej 2")
   print(f"pokud zase obsah a obvod 3 \n pro kruznici opsanou a vepsanou 4")
   while True:
    try:
         od=float(input(f"tak co?"))
         if od <=0 or od>=5:
            print(f"neplatne cislo zkus znova")
            continue
    except ValueError:
        print("Chyba! Zadej prosím číslo.")
        continue
    if od==1:
       strany_trojuhelniku(a,b,c)
       typ_troj(a,b,c)
       break
    if od==2:
       vykres(a,b,c)
       break
    if od==3 :
       obvod_a_obsah(a,b,c)
       break
    else:
       obsah=obvod_a_obsah(a,b,c)[1]
       kruh_vepsana_a_opsana(a,b,c,obsah)
       break
   print(f"bylo mi dnes potesenim")
   return




lobyy()

