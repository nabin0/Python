def gettime():
    import datetime
    return datetime.datetime.now()


nowtime = gettime()


def take(n):
    # For Harry
    if n == 1:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            val = input("Enter Your Exercise Here: ")
            with open('harry-exe.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")
        if c == 2:
            val = input("Enter Your Diet Here: ")
            with open('harry-diet.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")
    # For Larry
    elif n == 2:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            val = input("Enter Your Exercise Here: ")
            with open('larry-exe.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")
        if c == 2:
            val = input("Enter Your Diet Here: ")
            with open('larry-diet.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")
    #      For karry
    elif n == 3:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            val = input("Enter Your Exercise Here: ")
            with open('karry-exe.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")
        if c == 2:
            val = input("Enter Your Diet Here: ")
            with open('karry-diet.txt', 'a') as file:
                file.write(str(nowtime) + "   " + val + "\n")
            print("Written Successfully.")

    else:
        print("Please Enter Valid Input!!!")


def give(n):
    # For Harry
    if n == 1:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            print("Here Is your Exercise Data: \n")
            with open('harry-exe.txt') as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open('harry-diet.txt') as file:
                for i in file:
                    print(i, end="")
    if n == 2:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            print("Here Is your Exercise Data: \n")
            with open('lary-exe.txt') as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open('larry-diet.txt') as file:
                for i in file:
                    print(i, end="")
    if n == 3:
        c = int(input("Enter 1 For Exercise 2 For Diet"))
        if c == 1:
            print("Here Is your Exercise Data: \n")
            with open('karry-exe.txt') as file:
                for i in file:
                    print(i, end="")
        if c == 2:
            with open('karry-diet.txt') as file:
                for i in file:
                    print(i, end="")

    else:
        print("Please Enter Valid Input!!!")


a = int(input("Enter 1 For Add 2 For Retrieve"))
if a == 1:
    b = int(input("Enter 1 for Harry, 2 for larry, 3 fr karry"))
    take(b)
elif a == 2:
    b = int(input("Enter 1 for Harry, 2 for larry, 3 fr karry"))
    give(b)
