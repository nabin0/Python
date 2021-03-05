
# FAULTY CALCULATOR

print("TYPE\n (add) for addition\n (sub) for subtraction\n (mult) for multiplication\n (div) for division\n")
op = input()
num1 = int(input("enter first number:\n"))
num2 = int(input("enter second number:\n"))
add = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
if num1 == 56 and num2 == 9 and op == 'add':
    print("The sum of {} and {} is 77".format(num1, num2))
elif num1 == 45 and num2 == 3 and op == 'mult':
    print("The multiplication of {} and {} is 555".format(num1, num2))
elif num1 == 56 and num2 == 6 and op == 'div':
    print("The division of {} and {} is 4".format(num1, num2))
elif op == 'add':
    print("The addition of {} and {} is " .format(num1, num2), add)
elif op == 'sub':
    print("The subtraction of {} and {} is " .format(num1, num2), sub)
elif op == 'mult':
    print("The multiplication of {} and {} is " .format(num1, num2), mult)
elif op == 'div':
    print("The division of {} and {} is " .format(num1, num2), div)
else:
    print("Error! check your input")
