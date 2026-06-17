from modules.task import Task
from modules.taskmanager import Taskmanage


def menu():
    manager = Taskmanage()

    while True:
        print("\n--- MENU ---")
        print("1 - Přidat úkol")
        print("2 - Zobrazit všechny úkoly")
        print("3 - Filtrovat podle statusu")
        print("4 - Upravit úkol")
        print("5 - Změnit status")
        print("6 - Smazat úkol")
        print("7 - Uložit")
        print("8 - Načíst")
        print("9 - Konec")

        volba = input("Zadej volbu: ")

        # 1) PŘIDÁNÍ ÚKOLU
        if volba == "1":
            manager.novy_task()

        # 2) VÝPIS
        elif volba == "2":
            manager.seznam()

        # 3) FILTR
        elif volba == "3":
            status = input("Zadej status: ")
            vysledek = manager.seznam_dlestatus(status)
            print(vysledek)

        # 4) ÚPRAVA
        elif volba == "4":
            task_id = int(input("Zadej ID: "))
            title = input("Nový název (nech prázdné pokud nechceš měnit): ")
            description = input("Nový popis (nech prázdné pokud nechceš měnit): ")

            if title == "":
                title = None
            if description == "":
                description = None

            manager.uprav(task_id, title, description)

        # 5) STATUS
        elif volba == "5":
            task_id = int(input("Zadej ID: "))
            status = input("Nový status: ")
            manager.zmena_status_dleid(task_id, status)

        # 6) SMAZÁNÍ
        elif volba == "6":
            task_id = int(input("Zadej ID: "))
            manager.smaz(task_id)

        # 7) ULOŽIT
        elif volba == "7":
            manager.save_jas("data.json")

        # 8) NAČÍST
        elif volba == "8":
            manager.from_jas("data.json")

        # 9) KONEC
        elif volba == "9":
            print("Konec programu")
            break

        else:
            print("Neplatná volba")


menu()      