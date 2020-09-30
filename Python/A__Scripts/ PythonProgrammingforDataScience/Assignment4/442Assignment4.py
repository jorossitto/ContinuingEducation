
import re

def problem1():
    """Your task is to write a function to print valid phone numbers. You need to accept the inputs
from the file(input1.txt) and output the valid phone numbers on the console.
Format for valid phone numbers is:
(xxx) xxx-xxxx
xxx-xxx-xxxx
where x would be a number.
"""
    print("Problem 1")
    printPhoneNumber()
    return
def problem2():
    """You are given a file as an input. Your task is to transpose the contents of the file. The input
file may include uneven lines of whitespace which you need to handle. Note, the output
matrix should not have whitespaces.
Write a function to output the transposed content on the console as well as to an output file. """

    print("Problem 2\n")
    transpose()
    return
def problem3():
    """3. Your task is to create a library manager as a menu-driven console application. The system
should have the following functionalities in their menu:
i. Add books
ii. Remove books
iii. Add membership
iv. Remove membership
v. Rent book
vi. List books
vii. List members
viii. Exit
You need to create separate files to store information of books, members, book rentals.
When the system starts, it should import all contents of the file into the system, if the files are
not empty.
All-important fields should be checked for empty or incorrect format. Examples: name, DOB,
etc. should not be blank. Phone numbers should be a standard format, etc.
Also, you may add any other related functionality as well. """
    print("Problem 3\n")
    libraryManager()
    return
def problem4():
    """Complete the remaining tic-tac-toe game. Tic-tac-toe always has a square matrix. The game
would be in easy-mode, i.e. 3x3 matrix. You would be given positions of the already halfplayed game in input file. Your task is to first fill in the matrix from the positions given in the
file.
Then, you need to play for the remaining positions. In the end, you need to output the
possible winner(A or B) or Draw.
"""
    print("Problem 4")
    ticTacToe()

def ticTacToe():
    fileName = "input3.txt"
    fileContents = ReadFile(fileName)
    moves = dict()
    tempMoves = []
    won = False
    lastMove = ""
    #print(len(tempMoves))
    for i in range (0, 9, 1):
        tempMoves.append('=')
    for move in fileContents:
        moveAsInt = int(move[0]) - 1
        #print(moveAsInt)
        tempMoves[moveAsInt] = move[2]
        lastMove = move[2]

    while(won == False):
        # display board
        count = 0
        for move in tempMoves:
            count = count + 1
            print(move, '\t', end="")
            if (count % 3 == 0):
                print("")

        # ask for move
        if(lastMove == 'O'):
            lastMove = 'X'
        else:
            lastMove = 'O'
        spaceToMove = int(input("What space would you like to move to? "))
        tempMoves[spaceToMove] = lastMove

        #check for winner
        won = True


def libraryManager():
    printMenu()
    bookList = "bookList.txt"
    membershipList = "membershipList.txt"
    rentList = "rentList.txt"
    readRentals = ReadFile(rentList)
    readMembers = ReadFile(membershipList)
    readBooks = ReadFile(bookList)
    addBookMenu = "1"
    removeBookMenu = "2"
    addMembershipMenu = "3"
    removeMembershipMenu = "4"
    rentBookMenu = "5"
    listBookMenu = "6"
    listMembersMenu = "7"
    exitMenu = "8"

    loop = True
    menu = ""
    while(loop):
        menu = input("What would you like to do? Type menu to see the menu: ")
        if(menu == addBookMenu):
            # Add books
            addBooks(bookList, readBooks)
        elif(menu == removeBookMenu):
            #Remove books
            readBook = True
            value = ""
            while (readBook):
                try:
                    value = int(input("What book number would you like to remove? "))
                    value = value - 1
                    readBook = False
                except ValueError:
                    print("Please enter the bookID: ")
            print("Removing Book: ", readBooks[value])
            readBooks.pop(value)
            writeToFile(bookList, readBooks)
        elif (menu == addMembershipMenu):
            # Add membership
            nameQuestion = "What is the name of the member? "
            DOBQuestion = "Please enter DOB? "
            phoneQuestion = "What is the phone number? "
            name = checkBlanks(nameQuestion)
            DOB = checkBlanks(DOBQuestion)
            phoneNumber = checkBlanks(phoneQuestion)
            memberInfo = []
            memberInfo.append(name)
            memberInfo.append(DOB)
            memberInfo.append(phoneNumber)
            readMembers.append(memberInfo)
            print("Adding Members: ", readMembers)
            writeToFile(membershipList, readMembers)
        elif (menu == removeMembershipMenu):
            # Remove membership
            readMemberloop = True
            value = ""
            while (readMemberloop):
                try:
                    value = int(input("What book number would you like to remove? "))
                    value = value - 1
                    readMemberloop = False
                except ValueError:
                    print("Please enter the bookID: ")
            print("Removing Member: ", readMembers[value])
            readMembers.pop(value)
            writeToFile(membershipList, readMembers)
        elif (menu == rentBookMenu):
            # Rent book
            readMemberloop = True
            while (readMemberloop):
                try:
                    value = int(input("Who is renting the book? (use id)"))
                    value = value - 1
                    readMemberloop = False
                except ValueError:
                    print("Who is renting the book: (use id)")
            readBookLoop = True
            while (readBookLoop):
                try:
                    bookID = int(input("What book number would you like to rent? "))
                    bookID = bookID - 1
                    readBookLoop = False
                except ValueError:
                    print("Please enter the bookID: ")
            output = readMembers[value] + "Rented " + readBooks[bookID]
            readRentals.append(output)
            print("Adding Rentals: ", readRentals)
            writeToFile(rentList, readRentals)
        elif (menu == listBookMenu):
            # List books
            count = 0
            for book in readBooks:
                count = count + 1
                print(count, ": ", book)
        elif (menu == listMembersMenu):
            # List members
            count = 0
            for member in readMembers:
                count = count + 1
                #print("Name: ", member[0], " DOB: ", member[1], " Number: ", member[2])
                print(count, ": ", member)
        elif (menu == exitMenu):
            # Exit
            print("Thanks for using the Library Manager")
            loop = False
        elif (menu == "menu"):
            printMenu()
        else:
            print("I'm sorry I didn't understand, type menu to see the menu again.")
def addBooks(fileToAddBooksTo, fileContents):
    #fileContents = fileContents
    readBook = True
    book = input("What is the name of the book?")
    while (readBook):
        if (book == ""):
            book = input("Please enter the name of the book")
        if (book != ""):
            readBook = False
    fileContents.append(book)
    print("Adding Books: ", fileContents)
    writeToFile(fileToAddBooksTo, fileContents)
def checkBlanks(question):
    blank = True
    while(blank):
        answer = input(question)
        if(answer != ""):
            return answer
def printMenu():
    print("Press 1 to Add books")
    print("Press 2 to Remove books")
    print("Press 3 to Add membership")
    print("Press 4 to Remove membership")
    print("Press 5 to Rent book")
    print("Press 6 to List books")
    print("Press 7 to List members")
    print("Press 8 to Exit")
def printPhoneNumber():
    isPhoneNumber = False
    OpenAndReadFile("input1.txt")
    with open("input1.txt") as file:
        for line in file:
            isPhoneNumber = IsPhoneNumber(line)
            if(isPhoneNumber):
                print(line, end="")
def IsPhoneNumber(phoneNumber):
    pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    pattern2 = re.compile('[(]\d\d\d[)]\s\d\d\d-\d\d\d\d')
    match = pattern.match(phoneNumber)
    match2 = pattern2.match(phoneNumber)
    #print(type(match))
    if(match or match2):
        return True
    else:
        return False
def transpose():
    OpenAndReadFile("input2.txt")
    fileContents = []
    container = []

    #create a list of all the file contents broken up by words
    with open("input2.txt") as file:
        for line in file:
            if (line.isspace() == False):
                splitLine = line.split()
                fileContents.append(splitLine)
        #print(fileContents)
        container1 = []
        container2 = []
        container3 = []
        #look at the lines in the fileContents
        for line in fileContents:
            #look at the words in the lines
            for i in range(0, len(line), 1):
                #heapSort the words into the correct places
                heapSort = i % len(line)
                #print("Heapsort: ", heapSort, "line:", line[i])
                if(heapSort == 0):
                    container1.append(line[i])
                    #print("Container 1: " , container1)
                if(heapSort == 1):
                    container2.append(line[i])
                if(heapSort == 2):
                    container3.append(line[i])

        #print("Container 1: " , container1)

        #create the tuples then add them to the container
        container.append(tuple(container1))
        container.append(tuple(container2))
        container.append(tuple(container3))

        #print the output and write it to the file
        print(container)
    with open("output2.txt", "w") as file:
        file.write(str(container))
def writeToFile(fileName, whatToWrite):
    print("Adding to file: ", whatToWrite)
    with open(fileName, "w") as file:
        for item in whatToWrite:
            file.write("%s\n" % item)
def OpenAndReadFile(fileName):
    print("Input: ")
    with open(fileName) as file:
        for line in file:
            print(line, end="")

    print("\n\nOutput:")
def ReadFile(fileName):
    fileContents = []
    with open(fileName) as file:
        for line in file:
            #remove any extra line breaks
            if (line.isspace() == False):
                line = line.rstrip('\n')
                fileContents.append(line)
    print(fileName, "File Contents: ", fileContents)
    return fileContents

#problem1()
#problem2()
#problem3()
problem4()