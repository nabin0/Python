import random
import time


def guessTheNumber(a, b):
    actualNumber = random.randint(a, b)
    guess = int(input("Enter your Guess Here: "))
    noOfGuessToWin = 0
    while actualNumber != guess:
        if actualNumber < guess:
            guess = int(input("Your Guess is high. Select lower number."))
            noOfGuessToWin += 1
        else:
            guess = int(input("You guess is low. Select higher number."))
            noOfGuessToWin += 1

    print("You Have Guessed Correct Number")
    return noOfGuessToWin


if __name__ == "__main__":
    print("You have to Enter tow values and guess the number selected by computer between these inputs.")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the Second number: "))
    time.sleep(2)

    print("\nNow it's player 1's turn\n")
    p1 = guessTheNumber(a, b)
    print("\nNow it's player 2's turn\n")
    p2 = guessTheNumber(a, b)

    print("Calculating the result.")
    time.sleep(1)
    print("Please Wait...")
    time.sleep(2)
    if p1 > p2:
        print("Player 2 is WINNER!!!")
    elif p1 < p2:
        print("Player 1 is WINNER!!!")
    else:
        print("Tie between both player!!!")
