#---------------------------
def newGame():
    guesses = []
    correctGuess = 0
    questionNum = 1

    for key in questions:
        print("---------------------")
        print(key)
        for i in options[questionNum - 1]: 
            print(i)
        guess = input("Enter (A, B, C, D) : ")
        guess = guess.upper()
        guesses.append(guess)

        correctGuess += checkAnswer(questions.get(key), guess)
        questionNum += 1

    displayScore(correctGuess, guesses)
#---------------------------
def checkAnswer(anwser, quess):

    if anwser == quess:
        print("Correct")
        return 1
    else : 
        print ("Incorrect")
        return 0
#---------------------------
def displayScore(correctGuesses, guesses):
    print ("--------------------")
    print("Results: ")
    print("---------------------")
    print("Answers : ", end="")
    for i in questions: 
        print(questions.get(i), end=" ")
    print()
    print("Guesses : ", end="")
    for i in guesses: 
        print(i, end="")
    print()

    score = int((correctGuesses / len(questions)) * 100)
    print("Your Score is: " + str(score) + "%")
#---------------------------
def playAgain():
    response = input("Do you want to play again ( Yes/No): ").lower()
    if response == "yes":
        return True
    else:
        return False


questions = {
    "who created Python?" : "A",
    "What year was pyton created": "B",
    "Python is tributed to which comedy group" : "C" ,
    "Is the earth round": "A"
}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zackerburg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonly Island", "B. Smosh", "C. Monty Python", "D. SNL"],
            ["A. True", "B. False", "C. Sometimes", "D. What's earth"]]

newGame()
while playAgain():
    newGame()


print("Bye")
