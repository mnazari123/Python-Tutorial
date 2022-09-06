import random
while True:
    choices = ["rock" , "paper", "scissors"]

    computer  = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
        print ("Compute: ", computer)
        print ("Player: ", player)
        print ("tie!")
    elif player == "rock":
        if computer == "paper":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You lose!")
        if computer == "scissors":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You win!")
    elif player == "paper":
        if computer == "scissors":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You lose")
        if computer == "rock":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You wind")
    elif player == "scissors":
        if computer == "rock":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You lose")
        if computer == "paper":
            print ("Compute: ", computer)
            print ("Player: ", player)
            print ("You wind")
    play_again = input ("Play again (Yes/No)").lower()
    if play_again != "yes":
        break
print ("Bye")