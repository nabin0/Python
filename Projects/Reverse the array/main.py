# Built in method to reverse the list we have <list.reverse()> method too to reverse a list
def builtInReverseTheList(lst):
    revObj = reversed(lst)
    revList = [i for i in revObj]
    return revList

# Reversing a list by slicing the list


def reverseListBySlicing(lst):
    return lst[::-1]

# Reversing the list by swapping the value


def reverseListBySwapping(lst):
    startPtr = 0  # index pointer starts from index 0
    endPtr = len(lst) - 1  # index pointer starts from end of the list
    # Swapping elements of a list using while loop
    while startPtr < endPtr:
        temp = lst[startPtr]
        lst[startPtr] = lst[endPtr]
        lst[endPtr] = temp
        startPtr = startPtr + 1
        endPtr = endPtr - 1
    return lst

# One line method for swapping in python


def swapRev(lst):
    for i in range(len(lst)):
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
    return lst


if __name__ == "__main__":
    # Taking list as user input
    length = int(input("Enter the length of list."))
    print("Enter your list elements one by one.")
    lst = []
    for i in range(length):
        lst.append(int(input()))

    # Printing user's list
    print(f"Your list is: {lst}")

    # Invoiking reverse functuons
    print(builtInReverseTheList(lst))
    print(reverseListBySlicing(lst))
    print(reverseListBySwapping(lst))
    print(swapRev(lst))
