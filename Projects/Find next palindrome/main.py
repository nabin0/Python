# Function to find next palindrome
def nextPalindrome(num):
    while str(num) != str(num)[::-1]:
        num = num+1
    return num


if __name__ == "__main__":
    # Taking user input for test numbers whose corresponding palindrome will be provided them as result
    noOfTimes = int(input("How many elements palindrome you want to take:"))
    print("\nEnter the number for which you want corresponding palindrome number.")
    nums = []
    for i in range(noOfTimes):
        nums.append(int(input()))

    # Shwing corresponding palindrome number
    for num in nums:
        print(
            f"The next palindrome for number {num} is: {nextPalindrome(num)}")
