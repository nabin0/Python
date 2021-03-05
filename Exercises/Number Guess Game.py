    # GUESS THE NUMBER
number = 15
num_of_chance = 1
print("You have 5 chances and you have to guess the number using given hints")
while num_of_chance < 5:
    num = int(input("Enter the numbers\n"))
    if num > 15:
        print("You choose too high number")
    elif num < 15:
        print("you choose too low number")
    else:
        print("congratulation!! you have choosen correct number")
        break
    print(5 - num_of_chance, "chance left \n")
    num_of_chance = num_of_chance + 1

if num_of_chance == 5:
    print("you are out of chance try again!!!")