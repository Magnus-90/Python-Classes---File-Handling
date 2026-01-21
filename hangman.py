import random
import sys

random_words_list = [
    "python", "java", "javascript", "html", "css",
    "java", "swift", "kotlin", "ruby", "php",
    "typescript", "golang",
    "bash", "powershell",
    "sql"
]

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


def maingame():
    guessed_letters = []
    wordlength_userinput = 0
    inputs = 0
    word = random.choice(random_words_list) # Zufällige Auswahl
    word_display = ["_" for _ in word]
    wordlength = len(word)
    max_attempts = 8
    print("Das Spiel beginnt")
    print(" ".join(word_display))
    while wordlength_userinput < wordlength and inputs < max_attempts:
        userinput = input("Geben sie einen Buchstaben ein: ").lower()
        if userinput in guessed_letters:
            print(f"{userinput} hast du schon mal eingegeben")
            continue
        guessed_letters.append(userinput)
        if userinput in word:
            for index, letter in enumerate(word):
                if letter == userinput:
                    word_display[index] = userinput
                    wordlength_userinput = wordlength_userinput + 1
                    print("Buchstabe ist im Wort")
        else:
            inputs = inputs + 1
            print("Buchstabe war nicht im Wort")
        print(" ".join(word_display))
        print(f"Fehlversuche: {inputs} von {max_attempts}")
        print("")
        checkstage(inputs)

    if wordlength_userinput == wordlength:
        print("Gewonnen!")
    else:
        print("Verloren! Das Wort war:", word)
    
    userinput_play_again = input("Möchten sie weiter spielen? (y/n): ").lower()
    while userinput_play_again != "y" and userinput_play_again != "n":
        print("Eingabe Ungültig. Bitte geben sie y oder n ein.")
        userinput_play_again = input("Möchten sie weiter spielen? (y/n): ").lower()
    match userinput_play_again:
        case "y":
            maingame()
        case "n":
            sys.exit("Spiel wird beendet...")
startmenu()