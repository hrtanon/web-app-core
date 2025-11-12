import time
from random import randint, seed

def horse_race(horse_count, steps_to_win):
    """
    Jednodušší verze závodu koní.
    Každý kůň má náhodný krok (0 nebo 1) a výpis se zobrazuje přehledně po řádcích.
    """
    positions = [0] * horse_count
    finished = False
    round_num = 0

    while not finished:
        round_num += 1
        print(f"\nKolo {round_num}:")
        for i in range(horse_count):
            step = randint(0, 1)
            positions[i] += step
            print(f"Kůň {i+1}: {positions[i] * '*'}")

            if positions[i] >= steps_to_win:
                print(f"\n🏆 Kůň {i+1} vyhrál závod po {round_num} kolech!")
                finished = True
                break

        time.sleep(0.1)

if __name__ == "__main__":
    seed()
    horse_race(5, 20)
