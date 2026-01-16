import random

random_words_list = ["python", "java", "javascript", "typescript"]

def startmenu():
    print("Hangman Spiel")
    print("---------------")
    maingame()

def maingame():
    i = 0
    wordlength_userinput = 0
    inputs = 0
    word = random.choice(random_words_list) # Zufällige Auswahl
    word_display = ["_ " for _ in word]
    wordlength = len(word)
    max_attempts = len(word) + 2
    print("Das Spiel beginnt")
    print("-----------------")
    print(word.capitalize())
    print(" ".join(word_display))
    while wordlength_userinput < wordlength and inputs < max_attempts:
        userinput = input("Geben sie einen Buchstaben ein: ").lower()
        if userinput in word:
            for index, letter in enumerate(word):
                if letter == userinput:
                    word_display[index] = userinput
            print("Buchstabe ist im Wort")
            wordlength_userinput = wordlength_userinput + 1
            inputs = inputs + 1
        else:
            inputs = inputs + 1
            print("Buchstabe war nicht im Wort")


startmenu()