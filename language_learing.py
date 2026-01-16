import sys
import random
common_words_en_de = {
    "the": "der/die/das",
    "be": "sein",
    "to": "zu",
    "of": "von",
    "and": "und",
    "a": "ein",
    "in": "in",
    "that": "dass",
    "have": "haben",
    "I": "ich",
    "it": "es",
    "for": "für",
    "not": "nicht",
    "on": "auf",
    "with": "mit",
    "he": "er",
    "as": "als",
    "you": "du/Sie",
    "do": "tun",
    "at": "bei",
    "this": "dies",
    "but": "aber",
    "his": "sein",
    "by": "von/durch",
    "from": "von",
    "they": "sie",
    "we": "wir",
    "say": "sagen",
    "her": "ihr",
    "she": "sie",
    "or": "oder",
    "an": "ein",
    "will": "werden",
    "my": "mein",
    "one": "eins",
    "all": "alle",
    "would": "würde",
    "there": "dort",
    "their": "ihr",
    "is": "ist",
    "are": "sind",
    "was": "war",
    "were": "waren",
    "been": "gewesen",
    "has": "hat",
    "had": "hatte",
    "can": "können",
    "could": "könnte",
    "should": "sollte",
    "may": "dürfen",
    "might": "könnte",
    "who": "wer",
    "what": "was",
    "when": "wann",
    "where": "wo",
    "why": "warum",
    "how": "wie",
    "if": "wenn",
    "about": "über",
    "which": "welche",
    "them": "sie",
    "me": "mich",
    "him": "ihn",
    "your": "dein/Ihr",
    "its": "sein/ihr",
    "our": "unser",
    "than": "als",
    "then": "dann",
    "so": "also",
    "no": "nein",
    "yes": "ja",
    "up": "hoch",
    "out": "raus",
    "into": "in",
    "over": "über",
    "only": "nur",
    "new": "neu",
    "time": "Zeit",
    "people": "Menschen",
    "know": "wissen",
    "see": "sehen",
    "use": "benutzen",
    "make": "machen"
}

def startmenu():
    print("Language Learing")
    print("----------------")
    startmenu_input = input("Möchten sie das Game starten? (y/n): ")
    while startmenu_input != "y" and startmenu_input != "n" and startmenu_input != "N" and startmenu_input != "Y":
        startmenu_input = input("Eingabe Falsch (y/n): ")
    match startmenu_input:
        case "y":
            start_learning()
        case "Y":
            start_learning()
        case "n":
            sys.exit()
        case "N":
            sys.exit()

def start_learning():
    score = 0
    words = random.sample(list(common_words_en_de.items()), 10) # Zufällige Auswahl von 10 Wörtern
    print("Das Spiel beginnt")
    print("-----------------")
    for englisch, deutsch in words:
        answer = input(f"Was heisst {englisch} auf Deutsch?: ").lower()
        correct_answers = deutsch.lower().split("/")

        if answer in correct_answers:
            print("Richtig!\n")
            score += 1
        else:
            print(f"Falsch Richtige Antwort: {deutsch}\n")
    print("--------------------------------------")
    print(f"Spiel beendet! Dein Score: {score}/10")
startmenu()