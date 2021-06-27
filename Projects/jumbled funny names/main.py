import random
import time

# Function to jumble at names


def jumbleNames(names):
    fname = [name.split()[0] for name in names]
    lname = [name.split()[1] for name in names]
    jumbledNameList = [(f"{fname} {random.choice(lname)}")for fname in fname]
    return jumbledNameList


def displayNames(lst):
    for name in lst:
        print(name)


if __name__ == "__main__":
    num = int(input("Enter the num of name you want to enter: "))

    # Taking name in input
    names = []
    for i in range(num):
        names.append(input(
            "Enter name as, example: Ned Stark (first_name and Last_name with spacce to first name)"))
    print("The names You Entered: ")
    displayNames(names)

    time.sleep(2)

    print("\nNow printing Jumbled Names::")
    jNames = jumbleNames(names)
    displayNames(jNames)
