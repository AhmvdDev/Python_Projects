"""
This is a Rock Paper Scissors program
I will try to do the program by myself first, then I will look for guidance
"""
import random

print("=================================================")
print("===== Welcome to Rock, Paper, Scissors game =====")
print("=================================================")
print("Here are how to play:\n"
      "- There are Three rounds\n"
      "- in every round you can pick your move:\n"
      "- 1. Rock\n"
      "- 2. Paper\n"
      "- 3. Scissors\n"
      "- Then 'Computer' will pick its move\n"
      "- Rock beats Scissors\n"
      "- Paper beats Rock\n"
      "- Scissors beats paper\n")


compPoints = 0
playerPoints = 0
for count in range(3):
    playerMove = int(input("Pick your move: "))
    compMove = random.randint(1,3)
    if playerMove == 1:
        print("You: Rock")
        if compMove == 2:
            print("Computer: Paper")
            compPoints += 1
            print(playerPoints, "-", compPoints)
        elif compMove == 3:
            print("Computer: Scissors")
            playerPoints += 1
            print(playerPoints, "-", compPoints)
        else:
            print("Computer: Rock")
            print("Draw, ", playerPoints, "-", compPoints)
            continue
    elif playerMove == 2:
        print("You: Paper")
        if compMove == 1:
            print("Computer: Rock")
            playerPoints += 1
            print(playerPoints, "-", compPoints)
        elif compMove == 3:
            print("Computer: Scissors")
            compPoints += 1
            print(playerPoints, "-", compPoints)
        else:
            print("Computer: Paper")
            print("Draw", playerPoints, "-", compPoints)
            continue
    elif playerMove == 3:
        print("You: Scissors")
        if compMove == 1:
            print("Computer: Rock")
            compPoints += 1
            print(playerPoints, "-", compPoints)
        elif compMove == 2:
            print("Computer: Paper")
            playerPoints += 1
            print(playerPoints, "-", compPoints)
        else:
            print("Computer: Scissors")
            print("Draw", playerPoints, "-", compPoints)
            continue
    else:
        print("Invalid Choice")


if playerPoints > compPoints:
    print("Congrats, You Win!!")
elif compPoints > playerPoints:
    print("Hardluck :(")
else:
    print("Nice Try")

