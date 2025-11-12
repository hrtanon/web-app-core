from random import randint, seed

def horse_race(track_length, horses, max_steps, output=0):
    """
    Simuluje dostih několika koní.

    Každý kůň začíná na pozici 0 a v každém kroku se posune o 1–3 políčka vpřed náhodně.
    Kůň, který jako první dosáhne nebo překročí délku trati, vyhrává.
    Pokud po vyčerpání kroků nikdo nedoběhne, závod končí bez vítěze.

    Args:
        track_length (int): délka závodní dráhy (v polích)
        horses (int): počet koní
        max_steps (int): maximální počet kroků simulace
        output (int): 1 = vypisuje průběh, 0 = ticho

    Returns:
        str: jméno vítěze ("Horse_X") nebo "no_winner"
    """
    positions = [0] * horses

    for step in range(max_steps):
        for i in range(horses):
            move = randint(1, 3)
            positions[i] += move

            if positions[i] >= track_length:
                if output:
                    print(f"Kůň {i+1} doběhl do cíle v kroku {step+1}!")
                return f"Horse_{i+1}"

        if output:
            race_view = "".join(["🐎" + "-" * positions[i] for i in range(horses)])
            print(f"Krok {step+1}: {race_view}")

    if output:
        print("Závod skončil bez vítěze.")
    return "no_winner"


def horse_race_analysis(track_length, horses, max_steps, count):
    """
    Provede více simulací závodu a spočítá, kolikrát vyhrál který kůň.

    Args:
        track_length (int): délka závodní dráhy
        horses (int): počet koní
        max_steps (int): maximální počet kroků
        count (int): počet opakování závodu

    Returns:
        dict: výsledek počtu a procentuální úspěšnosti
    """
    results = {f"Horse_{i+1}": 0 for i in range(horses)}
    results["no_winner"] = 0

    for _ in range(count):
        result = horse_race(track_length, horses, max_steps)
        results[result] += 1

    total = count
    for key in results:
        results[key] = (results[key], round(results[key] / total * 100, 2))

    print(f"\nStatistika po {count} závodech:")
    for key, (cnt, pct) in results.items():
        label = "Bez vítěze" if key == "no_winner" else key
        print(f"{label:12}: {cnt:4}x ({pct:5.2f} %)")

    return results



if __name__ == "__main__":
    seed(42)
    horse_race_analysis(track_length=50, horses=5, max_steps=30, count=100)
