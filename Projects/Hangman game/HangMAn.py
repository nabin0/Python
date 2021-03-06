# Welcome To Hangman


import random
import time

print("Welcome To Hangman\n")
name = input("Please Enter Your Name:")
time.sleep(1)
print(f"Hello {name}! Best of luck")
time.sleep(1)
print("The Game is loading...")
time.sleep(1)
print("Lets Play The Game\n")
time.sleep(1)


# Initialize useful variables


def main():
    global word
    global count
    global display
    global length
    global already_guessed
    global play

    words_to_select = ["hola", "delhi", "april", "mice", "coma", "lite", "fun", "funny", "hello", "umbrella"]
    word = random.choice(words_to_select)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play = ""


def game_loop():
    global play
    play = input("Enter 'Y' to replay game and 'N' to quiet the game.\n")
    while play not in ['n', 'y', 'N', 'Y']:
        play = input("Enter 'Y' to replay game and 'N' to quiet the game.\n")
    if play == 'y' or play == 'Y':
        main()
        game_body()
    elif play == 'n':
        print("Thanks For Playing.")
        exit()


def game_body() -> object:
    global display
    global count
    global word
    global already_guessed
    limit = 5
    guess = input(f"This Is Computers guess {display} Enter Your Guess.\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Please Try A Letter.\n")
        game_body()

    elif guess in word:
        already_guessed.extend([guess])

        for index, item in enumerate(word):
            if item == guess:
                index_of_guess = index
                display = display[:index_of_guess] + guess + display[index_of_guess + 1:]
                word = word[:index_of_guess] + '_' + word[index_of_guess + 1:]
                print(display + "\n")

    elif guess in already_guessed:
        print("Already Entered Try Another Letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print(" ____ \n"
                  "|    \n"
                  "|    \n"
                  "|    \n"
                  "|    \n"
                  "|    \n")
            print(f"This Guess IS Wrong. Number Of Chance left: {limit - count}. Try Again..\n")

        elif count == 2:
            time.sleep(1)
            print(" ____ \n"
                  "|    | \n"
                  "|    \n"
                  "|    \n"
                  "|    \n"
                  "|    \n")
            print(f"This Guess IS Wrong. Number Of Chance left: {limit - count}. Try Again..\n")

        elif count == 3:
            time.sleep(1)
            print(" ____\n"
                  "|    |\n"
                  "|    |\n"
                  "|    \n"
                  "|    \n"
                  "|    \n")
            print(f"This Guess IS Wrong. Number Of Chance left: {limit - count}. Try Again..\n")

        elif count == 4:
            time.sleep(1)
            print(" ____ \n"
                  "|    |\n"
                  "|    |\n"
                  "|    O \n"
                  "|    \n"
                  "|    \n")
            print(f"This Guess IS Wrong. Number Of Chance left: {limit - count}. Try Again..\n")

        elif count == 5:
            time.sleep(1)
            print(" ____\n"
                  "|    |\n"
                  "|    |\n"
                  "|    O\n"
                  "|   /|\ \n"
                  "|   /|\ \n")
            print("You are Hanged!!!")
            print(f"The Word was {already_guessed}, {word}")
            game_loop()

    if word == '_' * length:
        print("You Have Won ")
        game_loop()

    elif count != limit:
        game_body()


main()

game_body()
