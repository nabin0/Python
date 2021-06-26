class Library:
    def __init__(self, libraryName, booksList) -> None:
        self.libraryName = libraryName
        self.booklist = booksList
        self.lendBookDict = {}

    def displayBook(self):
        for book in self.booklist:
            print(book)

    def lendBook(self, username, bookname):
        if bookname not in self.lendBookDict.keys() and bookname in self.booklist:
            self.lendBookDict.update({bookname:username})
            self.booklist.remove(bookname)
        elif bookname not in self.booklist:
            print("No such book is available in this library.")
        else:
            print(f"this book is already taken by {self.lendBookDict[bookname]}")

    def addBook(self, bookname):
        self.booklist.append(bookname)

    def returnBook(self, bookname):
        if bookname not in self.lendBookDict.keys():
            print("No such book was taken from this library..")
        self.lendBookDict.pop(bookname)
        self.booklist.append(bookname)


if __name__ == "__main__":
    ned = Library("Centeral Library", ["python", "C++", "java"])
    print(f"welcome to {ned.libraryName} ")
    while(True):
        print(f"""Please select any from given options:\n 1.Display Books\n 2. Lend Book \n 3. Add Book \n 4. Return Book """)
        userInp = input("Enter your input here: ")
        userInp = int(userInp)
        if userInp == 1:
            ned.displayBook()
        elif userInp == 2:
            username = input("Enter your name:")
            bookname = input("Enter The name of book you want:")
            ned.lendBook(username, bookname)
        elif userInp == 3:
            bookname = input("Enter The name of book you want to add:")
            ned.addBook(bookname)
        elif userInp == 4:
            bookname = input("Enter The name of book you want to return:")
            ned.returnBook(bookname)
        else:
            print("Wrong input please enter valid input!!")

        userInp = ""
        while userInp != "c" and userInp != "q":
            userInp = input("Enter 'q' to quit or 'c' to continue")
            if userInp == "c":
                continue
            elif userInp == "q":
                exit()
            else:
                print("Please enter valid input")
