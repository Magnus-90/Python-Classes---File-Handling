import sys
questions = [
    {
        "question": "Welche Automarke ist nicht von Deutschland?",
        "options": ["BMW", "Audi", "Toyota", "Mercedes"],
        "answer": "C"
    },
    {
        "question": "Welches Land hat die meisten Zeitzonen?",
        "options": ["USA", "Russland", "Frankreich", "China"],
        "answer": "C"
    },
    {
        "question": "Was ist das teuerste Gewürz?",
        "options": ["Safran", "Vanille", "Pfeffer", "Zimt"],
        "answer": "A"
    },
    {
        "question": "Wie viele Ringe sind auf der Olympischenflagge?",
        "options": ["4", "5", "6", "7"],
        "answer": "B"
    },
    {
        "question": "Was ist das meistverkaufte Videospiel?",
        "options": ["Minecraft", "Tetris", "GTA V", "FIFA"],
        "answer": "A"
    },
    {
        "question": "Wer entdeckte 1492 Amerika?",
        "options": ["Christoph Kolumbus", "Amerigo Vespucci", "Ferdinand Magellan", "Leif Eriksson"],
        "answer": "A"
    },
    {
        "question": "Wie viele Saiten hat eine Standard-Gitarre?",
        "options": ["4", "5", "6", "7"],
        "answer": "C"
    },
    {
        "question": "Wie viele Felder hat ein Schachbrett?",
        "options": ["64", "72", "81", "100"],
        "answer": "A"
    },
    {
        "question": "Wer ist der erfolgreichste Schweizer Tennisspieler?",
        "options": ["Roger Federer", "Stan Wawrinka", "Martina Hingis", "Belinda Bencic"],
        "answer": "A"
    },
    {
        "question": "Wie viele Nullen hat eine Million?",
        "options": ["3", "6", "9", "12"],
        "answer": "B"
    }
]

def startmenu():
    print("Quizgame")
    print("-------------------\n")
    startmenu_input = input("Möchten sie das Game starten? (y/n): ")
    while startmenu_input != "y" and startmenu_input != "n":
        startmenu_input = input("Eingabe Falsch (y/n): ")
    if startmenu_input == "y":
        startquiz()
    if startmenu_input == "n":
        sys.exit()

def startquiz():
    score = 0
    for question in questions:
        print("\n" + question["question"])
        showanswers(
            question["options"][0],
            question["options"][1],
            question["options"][2],
            question["options"][3]
        )
        user_answer = getuseranswer()

        if user_answer.upper() == question["answer"]:
            print("Richtig!")
            score += 1
        else:
            print("Falsch! Richtige Antwort:", question["answer"])

    print("\nQuiz beendet!")
    print(f"Dein Score: {score} von 10")

def showanswers(answer1, answer2, answer3, answer4):
    print("Auswahl:")
    print("A", answer1)
    print("B", answer2)
    print("C", answer3)
    print("D", answer4)

def getuseranswer():
    userquestion_input = input("Geben Sie Ihre Vermutung ein (A,B,C,D): ").upper()
    while userquestion_input not in ["A", "B", "C", "D"]:
        userquestion_input = input("Falsche Eingabe! (A,B,C,D): ").upper()
    return userquestion_input

startmenu()