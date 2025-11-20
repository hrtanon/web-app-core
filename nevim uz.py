import random

def sim_once():
    pole = ["."] * 11
    a = 5
    pole[a] = "*"
    kroky = 0

    while True:
        krok = random.choice([+1, -1])

        pole[a] = "."
        a = max(0, min(10, a + krok))
        pole[a] = "*"
        kroky += 1

        if a in (0, 10):
            return a, kroky


# statistika
vlevo = 0
vpravo = 0
souhrn_kroku = []

pocet_pokusu = 5000

for _ in range(pocet_pokusu):
    konec, kroky = sim_once()
    souhrn_kroku.append(kroky)
    if konec == 0:
        vlevo += 1
    else:
        vpravo += 1


print("Pocet pokusu:", pocet_pokusu)
print("Vlevo :", vlevo)
print("Vpravo:", vpravo)
print("Prumerny pocet kroku:", sum(souhrn_kroku) / pocet_pokusu)
print("Max:", max(souhrn_kroku))
print("Min:", min(souhrn_kroku))
