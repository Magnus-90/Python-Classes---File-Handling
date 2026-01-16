import random
import sys

random_words_list = ["python", "java", "javascript", "typescript", "html", "swift", "ruby"]

def startmenu():
    print("Hangman Spiel")
    print("---------------")
    maingame()

def maingame():
    guessed_letters = []
    i = 0
    wordlength_userinput = 0
    inputs = 0
    word = random.choice(random_words_list) # Zufällige Auswahl
    word_display = ["_" for _ in word]
    wordlength = len(word)
    max_attempts = len(word) + 2
    print("Das Spiel beginnt")
    # print(word.capitalize())
    print(" ".join(word_display))
    while wordlength_userinput < wordlength and inputs < max_attempts:
        userinput = input("Geben sie einen Buchstaben ein: ").lower()
        if userinput in guessed_letters:
            print(f"{userinput} hast du schon mal eingegeben")
            continue
        guessed_letters.append(userinput)
        inputs = inputs + 1
        if userinput in word:
            anzahl = word.count(userinput)
            for index, letter in enumerate(word):
                if letter == userinput:
                    word_display[index] = userinput
                    wordlength_userinput = wordlength_userinput + 1
                    print("Buchstabe ist im Wort")
        else:
            inputs = inputs + 1
            print("Buchstabe war nicht im Wort")
        print(" ".join(word_display))
        print(f"Versuche: {inputs}/{max_attempts}")
        print("")

    if wordlength_userinput == wordlength:
        print("Gewonnen!")
    else:
        print("Verloren! Das Wort war:", word)
    
    userinput_play_again = input("Möchten sie weiter spielen? (y/n): ").lower()
    while userinput_play_again != "y" and userinput_play_again != "n":
        print("Eingabe Ungültig. Bitte geben sie y oder n ein.")
    match userinput_play_again:
        case "y":
            maingame()
        case "n":
            sys.exit("Spiel wird beendet...")
startmenu()