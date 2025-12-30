import sys
import datetime

budget = {}
budget["transaktionen"] = []

counter = 0

def startmenu():
    print("Budget Tracker")
    print("----------------------\n")
    while True:
        try:
            budget_start = int(input("Geben Sie Ihr Budget ein: "))
            if budget_start < 0:
                print("Budget kann nicht unter 0 sein")
                continue
            break
        except ValueError:
            print("Bitte eine Zahl eingeben!")
    budget["budget_start"] = budget_start
    budget["budget_rest"] = budget_start
    mainmenu(budget_start)

def mainmenu(budget_start):
    budget_start = budget_start
    while True:
        print("Menu")
        print("-------------------------------")
        print("|    Optionen:                |")
        print("|    1. Ausgabe Erfassen      |")
        print("|    2. Budget Verlauf öffnen |")
        print("|    3. Programm Beenden      |")
        print("-------------------------------")
        try:
            user_mainmenu_input = int(input("Option wählen: "))
        except ValueError:
            print("Bitte eine Zahl eingeben!")
            continue
        match user_mainmenu_input:
            case 1:
                ausgabe_erfassen()
            case 2:
                budget_anzeigen()
            case 3:
                programm_exit()
            case _:
                print("Bitte eine Option wählen: (1,2,3)")

def ausgabe_erfassen():
    print("Ausgabe erfassen:")

    budget_description = input("Geben sie einen Namen für die Transaktion ein: ")
    while len(budget_description.strip()) == 0:
        print("Der Name kann nicht leer sein!")
        budget_description = input("Geben sie einen Namen für die Transaktion ein: ")
    while True:
        try:
            budget_ausgaben = float(input("Geben sie ihre Ausgabe ein: "))
            if budget_ausgaben <= 0:
                print("Ausgabe muss positiv sein!")
                continue
            break
        except ValueError:
            print("Bitte eine gültige Zahl eingeben!")

    budget["budget_rest"] -= budget_ausgaben
    budget["transaktionen"].append({
        "id": datetime.datetime.now(),
        "beschreibung": budget_description,
        "ausgaben": budget_ausgaben,
        "restbudget": budget["budget_rest"]
    })

def budget_anzeigen():
    print("Budget Verlauf:")
    print(f"Startbudget: {budget['budget_start']}, Restbudget: {budget['budget_rest']}")
    for t in budget["transaktionen"]:
        print(f"{t['id']}: {t['beschreibung']} - Ausgabe: {t['ausgaben']} - Restbudget: {t['restbudget']}")

def programm_exit():
    sys.exit("Programm wurde Beendet")

startmenu()