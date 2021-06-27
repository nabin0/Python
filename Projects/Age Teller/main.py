age = int(input("Enter your age or date of birth here."))
currentYear = 2021

if age < 100 and age > 0:
    bornYear = currentYear - age
    dateToBe100 = bornYear + 100
    print("You will be 100 by " + str(dateToBe100))

elif age <= 100:
    print("You are already 100.")

elif 2021 > age > 1921:
    dateToBe100 = age + 100
    bornYear = age
    print("You will be 100 by " + str(dateToBe100))

elif 1921 >= age:
    print("You are already 100")

elif age >= currentYear:
    print("You kidding buddy you are not born yet.")
    exit()

else:
    print("Invalid Input try again!!!")

yearValToKnowAge = int(input("Enter the value of year you want to know what your age will be."))

print("You will be " + str(yearValToKnowAge - bornYear))
