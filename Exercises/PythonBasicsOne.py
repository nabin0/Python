
# ---These are the list of programs for basic python learner/ reference



"""
# Program that computes value n+nn+nnn where n is given by user

n = int(input("Enter a integer: "))
l1 = int('%s' % n)
l2 = int("%s%s" % (n, n))
l3 = int("%s%s%s" % (n, n, n))

print(l1+l2+l3)
"""


"""
def value(n):
    '''Python program returns difference if less than 17 and double abs value if greater than 17'''
    if n <= 17:
        return 17 - n
    else:
        print( "The Value is", (n - 17) * 2);

elem1 = value(2)
print(elem1)
elem2 = value(21)
"""


"""
# Prints whether the number lies between this range or not
def lies(n):
    if 100 <= n < 1000:
        print("Number lies Between 100 to 1000")

    elif 1000 <= n < 2000:
        print("Number Lies Between 1000 And 2000")

    else:
        print("Number Doesn't Lies Between 100 And 2000")


num1 = lies(120)
num2 = lies(1200)
num3 = lies(12000)
 """


"""
# Sum with some little logic
def sumComd(a,b,c):
    sum = a + b +c
    if a == b == c:
        return sum * 3

    return sum


inp1 = sumComd(12,31,4)
print(inp1)

inp2 = sumComd(2,2,2)
print(inp2)
"""


"""
# append IS before string if it does not start with IS
def makeString(str):
    line = str.capitalize()
    if line.startswith("Is"):
        print(line)
    else:
        print("Is",line)


l1 = makeString("Ram A Human.")
l2 = makeString("is That Hello")

"""


"""
# Print String N times
def printString(str, n):
    result = ""
    for i in range(n):
        result = result + str
    print(result)

a1 = printString("Helllo iam Nabin.", 12)
"""


"""
# Number is Odd Or Even
def odVen(num):
    if (num % 2) == 0:
        print("The Number Is Even")

    else:
        print("The Number is odd")


num1 = odVen(2)
num2 = odVen(5)
"""


"""
# Count Number Of 4 Present in A list Or Array
def array(lst):
    count = 0
    for num in lst:
        if num == 4:
            count = count + 1
    return count


l1 = array([12, 4, 4, 121, 4, 31])
print(l1)
"""


"""
# Prints First 2 Letters of string n times
def strng(str, n):
    if len(str) <= 2:
        return str * n
    else:
        return str[0:2]*n + str

st1 = strng("hi", 4)
print(st1)
st2 = strng("Hello Iam Nabin.", 6)
print(st2)
"""


"""
# Histogram Pattern
def histogram(item):
    for n in item:
        output = ''
        num = n
        while num > 0:
            output += '*'
            num = num -1
        print(output)


h1= histogram([4, 5, 3, 6])

"""


"""
# Concatinate List items
def concatinate(lst):
    result = ''
    for elem in lst:
        result += str(elem)
    print(result)

lst1 = concatinate(["my", "Name" , 3, 45])

"""


"""
# Find Evens and prints Until 57 comes
def findEven(lst):
    for x in lst:
        if x == 57:
            break
        elif x % 2 == 0:
            print(x)

lst1 = findEven([12, 121, 14, 54, 1009, 198, 2, 92, 88, 57, 4, 6, 68, 66, 54, 131, 123])
"""


"""
# GCD(Greatest Common Divisor) Finder
def gcd(num1,num2):
    gcd = 1

    if num1 % num2 == 0:
        return num2

    for i in range(int(num2 / 2), 0, -1):
        if (num1 % i == 0) & (num2 % i == 0):
            gcd = i
            break
    return gcd


a = int(input("Enter The Input For First Number: \n"))
b = int(input("Enter The Input For Second Number: \n"))
print(gcd(a,b))

"""



"""
# Pr0gram To print Future Value of Principle With Time And Interest
def principleValue(principle, time, rate):
    FutureValPrinciple = (principle * (1 + ( rate/100)) ** time)
    return f"The Future Value of Principle {principle} with interest Rate of {rate}% and in time {time} will be: {round(FutureValPrinciple)}"

print(principleValue(10000, 7, 3.5))
"""


"""
# Distance Between Two Points
import math
def distance_btn_two_points(x1,y1,x2,y2):
    temp_distance = ((x2 - x1)**2) + ((y2 - y1) ** 2)
    distance = math.sqrt(temp_distance)
    return f"The Distance Between two points is: {distance}."


x1 = int(input("Enter The Value Of x1: \n "))
y1 = int(input("Enter The Value Of y1: \n "))
x2 = int(input("Enter The Value Of x2: \n "))
y2 = int(input("Enter The Value Of y2: \n "))

print(distance_btn_two_points(x1,y1,x2,y2))
"""


"""
# Check if File exist or not
import os

open("new.txt", "r")
print(os.path.isfile("new.txt"))
"""


"""
# Printing Architecture of current system
import platform
import os

print(platform.architecture())
print(os.uname())
"""


"""
# Print sitePackages
import site
print(site.getsitepackages())
"""


"""
# Execute Exxternal commands using python
import subprocess
subprocess.call(["ls", "-l"])
"""


"""
# Print Current running Path
import os
print(os.path.realpath(__file__))
"""



"""
# Number of cpus
import multiprocessing
print(multiprocessing.cpu_count())
"""


"""
# Converts Celsius into Fahrenheit and vice versa
inp = input("Enter The Temperature to be convert (e.g: 12C, 34F ) :")
inp_temperature = inp[:-1]
inp_convention = inp[-1]

if inp_convention.upper() == "C":
    result = round((int(inp_temperature) * 9) / 5 + 32)
elif inp_convention.upper() == "F":
    result = round((int(inp_temperature) - 32) * 5 / 9)
else:
    print("Please Check Input/Notation")
    quit()
print(f"The Temperature in {inp_convention} is: {result}")

"""


"""
# Create Patterns like histogram
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(6, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

"""


"""
# Histogram 
_list = [1, 12, 8, 3, 15, 6, 43, 2, 21, 11, 1, 1, 12, 121]

for i in _list:
    for j in range(i):
        print("*", end="")
    print("")

"""


"""
# Count Even And Odd Numbers
nums = (12, 121, 12, 234, 436, 56, 23, 12, 5, 454, 7, 123, 23, 12)
even_nums = 0
odd_nums = 0

for num in nums:
    if num % 2 == 0:
        even_nums += 1
    elif num % 2 != 0:
        odd_nums += 1
    else:
        print("Please Enter Numbers!!")

print(f"Number Of:\nEven: {even_nums}\nOdds: {odd_nums}")

"""


"""
# Type Of items
datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for items in datalist:
    print(f"The item is {items}, and type of {items} is: {type(items)}")
"""


"""
# Fibonacii
x, y = 0, 1

while y < 50:
    print(y)
    x, y = y, x + y

"""


