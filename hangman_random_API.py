import random
import sys
import zufallsworte as zufall

def startmenu():
    print("Hangman Spiel")
    print("---------------")
    maingame()

Hangman_Stages = [
    # 0
    """
    
    
    
    
    """,
    # 1
    """
      |
      |
      |
      |
    """,
    # 2
    """
      -----
      |
      |
      |
      |
    """,
    # 3
    """
      -----
      |  O
      |
      |
      |
    """,
    # 4
    """
      -----
      |  O
      |  |
      |
      |
    """,
    # 5
    """
      -----
      |   O
      |  /| 
      |
      |
    """,
    # 6
    """
      -----
      |   O
      |  /|\\
      |
      |
    """,
    # 7
    """
      -----
      |   O
      |  /|\\
      |  /
      |
    """,
    # 8
    """
      -----
      |   O
      |  /|\\
      |  / \\
      |
    """
]

def checkstage(inputs):
    print(Hangman_Stages[inputs])

def replaceumlaute(word):
    replacements = {
        "ä": "ae", # umlaut: ersatz
        "ö": "oe",
        "ü": "ue",
        "ß": "ss"
    }
    for umlaut, ersatz in replacements.items():
        word = word.replace(umlaut, ersatz)
    return word

def maingame():
    guessed_letters = []
    wordlength_userinput = 0
    inputs = 0
    word = zufall.anzahl_buchstaben(5, 1)[0] # Erste Zahl für Anzahl Buchstaben und Zweite Zahl für Anzahl Wörter
    word = replaceumlaute(word)
    word = word[0].lower() + word[1:]
    word_display = ["_" for _ in word]
    wordlength = len(word)
    max_attempts = 8
    print("\033[32mDas Spiel beginnt\033[0m")
    print(" ".join(word_display))
    while wordlength_userinput < wordlength and inputs < max_attempts:
        userinput = input("Geben sie einen Buchstaben ein: ").lower()
        userinput_length = len(userinput)
        if userinput_length > 1:
            print("\033[31mBitte nur einen Buchstaben gleichzeitig eingeben\033[0m")
            continue
        if userinput in guessed_letters:
            print(f"\033[31m{userinput} hast du schon mal eingegeben\033[0m")
            continue
        guessed_letters.append(userinput)
        if userinput in word:
            for index, letter in enumerate(word):
                if letter == userinput:
                    word_display[index] = userinput
                    wordlength_userinput = wordlength_userinput + 1
                    print("\033[42mBuchstabe ist im Wort\033[0m")
        else:
            inputs = inputs + 1
            print("\033[31mBuchstabe war nicht im Wort\033[0m")
        print(" ".join(word_display))
        print(f"\033[31mFehlversuche: {inputs} von {max_attempts}\033[m")
        print("")
        checkstage(inputs)

    if wordlength_userinput == wordlength:
        print("\033[32mGewonnen!\033[0m")
    else:
        print("\033[31mVerloren!\033[0m Das Wort war:", word)
    
    userinput_play_again = input("Möchten sie weiter spielen? (y/n): ").lower()
    while userinput_play_again != "y" and userinput_play_again != "n":
        print("\033[41mEingabe Ungültig. Bitte geben sie y oder n ein.\033[0m")
        userinput_play_again = input("Möchten sie weiter spielen? (y/n): ").lower()
    match userinput_play_again:
        case "y":
            maingame()
        case "n":
            sys.exit("\033[31mSpiel wird beendet...\033[0m")
startmenu()