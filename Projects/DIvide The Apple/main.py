print("Enter the number of apple your friend have: ")
noOfApple = int(input())
mn = int(input("Enter the min range: "))
mx = int(input("Enter the maximum range: "))

if mn == mx:
    print("This is not a range")
    if noOfApple % mn == 0:
        print(f"{mn} is divider of {noOfApple}")
    print("{mn} is not divider of {noOfApple}")

elif mn > mx:
    print("You Entered values in opposite order..BTW Here is your result")
    mnMxRange = [i for i in range(mx, mn)]
    for i in mnMxRange:
        if noOfApple % i == 0:
            print(f"{i} is divider of {noOfApple}")
        else:
            print(f"{i} is not divider of {noOfApple}")

else:
    mnMxRange = [i for i in range(mn, mx)]
    for i in mnMxRange:
        if noOfApple % i == 0:
            print(f"{i} is divider of {noOfApple}")
        else:
            print(f"{i} is not divider of {noOfApple}")
