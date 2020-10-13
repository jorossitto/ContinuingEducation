
def problem1():
    "A program to display a pattern of stars"
    rows = 5
    starsLeftAligned(rows)
    StarsRightAligned(rows)
    StarsCenterAligned(rows)
    return

def problem2():
    """We add a Leap Day on February 29, almost every four years. The leap day is extra and we add it
to the shortest month of the year, February.
There are three criteria to identify leap years:
1. The year can be evenly divided by 4;
2. If the year can be evenly divided by 100, it is NOT a leap year, unless;
3. The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap‐years, while 1800,
1900, 2100, 2200, 2300 and 2500 are NOT leap‐years.
Your task is to write a program with a function to verify whether the integer is a leap year or
not. The function should return True/False. """

    leapYearCheck = leapYearChecker(2)
    leapYearCheck = leapYearChecker(4)
    leapYearCheck = leapYearChecker(100)
    leapYearCheck = leapYearChecker(400)
    leapYearCheck = leapYearChecker(2000)
    leapYearCheck = leapYearChecker(2100)

def problem3():
    """International Morse Code defines a standard encoding where each letter is mapped to a
series of dots and dashes, as follows: "a"maps to ".‐", "b" maps to "‐...", "c" maps to "‐
.‐.", and so on. """
    morseCodeConverter()

def problem4(number):
    """Given a positive integer, output its 2’s complement number. The 2’s complement strategy is
to flip the bits of its binary representation and then add 1 to the binary representation.
You need to write the definition for the method find2sComplement().
Definition for findComplement() is already provided."""

    if(number != 0):
        binaryFlip(number)
    binaryFlip(10)
    binaryFlip(5)

def problem5(string):
    """Consider a robot at position (0, 0). Given a sequence of its moves, judge if this robot makes
a circle, which means it moves back to the original place.
4
The move sequence is represented by a string. And each move is represented by a
character. The valid robot moves are R (Right), L(Left), U (Up) and D (down).
Write a function to verify if the robot makes a circle. The output should be True or False. """
    string1 = "UD"
    string2 = "LDRRLRUULR"
    string3 = "RRDD"
    robotCircle(string1)
    robotCircle(string2)
    robotCircle(string3)
    
    if(string != ""):
        robotCircle(string)

def problem6():
    """Ask the user for a number, then a word, and then print out a phrase that depends on the
number and the word. You should pluralize the word by adding an “s” to the end whenever
they enter a number that is 0 or greater than 1."""
    MakePlural(10, "life")
    MakePlural(9, "bush")
    MakePlural(8, "church")
    MakePlural(7, "cactus")
    MakePlural(6, "guy")
    MakePlural(5, "toy")
    MakePlural(4, "key")
    MakePlural(3, "way")
    MakePlural(2, "fly")
    MakePlural(1, "hat")
    MakePlural(0, "hat")
    MakePlural(-1, "hat")

def problem7(number):
    """Write a function is_prime that takes in one integer as an argument and determines whether it is
a prime number or not. As a reminder, a prime number is only divisible by 1 and itself. is_prime
should return True or False depending on whether the number is prime. """
    is_prime(9)
    is_prime(7)
    is_prime(1)
    is_prime(number)

def problem8(string):
    """Write a function snake_case that takes in a string in camelCase (like you would write variables in
JavaScript), and converts it to snake_case, converting everything to lowercase and separating by
underscores. You can assume that each capital letter is the start of a new word. Use string
slicing to get “parts” of a word. """
    snake_case("snakeCase")
    snake_case("lookOverThere")
    snake_case("already_perfect")
    snake_case(string)

def problem9():
    """Write a function get_number_input that takes in a string as the prompt and uses that prompt to
ask the user for input using input(). However, in this function, you must ensure that the user
enters a number (int or float); otherwise, it must ask the question again. Return the user’s input
only when they enter a valid number. It should be able to accept negative numbers and decimal
points. """
    get_number_input()

#problem 1 start
def starsLeftAligned(numberOfRows):
    star = "*"
    space = " "
    print("Stars Left Aligned")
    for stars in range(0, numberOfRows):
        print(star)
        star = star + "*"

def StarsRightAligned(numberOfRows):
    star = "*"
    space = " "
    countdown = numberOfRows-1
    print("Stars Right Aligned")
    for stars in range(0, numberOfRows):
        print(space * countdown, star)
        countdown = countdown -1
        star = star + "*"

def StarsCenterAligned(numberOfRows):
    star = "**"
    space = " "
    countdown = numberOfRows-1
    print("Stars Center Aligned")
    for stars in range(0, numberOfRows):
        print(space * countdown, star * (stars+1))
        countdown = countdown -1
#problem 1 end

def leapYearChecker(year):
    if (year % 400 == 0):
        print(year, "is a leap year, returning True")
        return True
    if (year % 4 == 0 and year % 100 != 0):
        print(year, "is a leap year, returning True")
        return True
    print(year, "is not a leap year, returning False")
    return False

def binaryFlip(number):
    print("Your Number:", number)
    print("Your Number in Binary ",bin(number)[2:])
    base2Conversion = bin(number)[2:]
    string = "" + str(base2Conversion)
    finalString = ""
    for letter in string:
        if (letter == "0"):
            finalString = finalString + "1"
        elif (letter == "1"):
            finalString = finalString + "0"
    print("Your numbers binary flip", finalString)
    find2sComplement(int(finalString))

def find2sComplement(binary):
    decimal = 0
    tensPlace = 0
    while (binary != 0):
        dec = binary % 10 # get the remainder
        decimal = decimal + dec * pow(2, tensPlace) #add your number to your current total
        binary = binary // 10 #devide your binary by the power of 10
        tensPlace += 1 #add one to the tens place to convert next digit

    print("Your two's complement:", decimal + 1)

def robotCircle(stringRLUD):
    print("Input:", stringRLUD)
    startingPoint = [0, 0]
    endingPoint = [0, 0]
    for letter in stringRLUD:
        if letter.lower() == "r":
            endingPoint[0] = endingPoint[0] + 1
            #print(endingPoint)
        if letter.lower() == "l":
            endingPoint[0] = endingPoint[0] - 1
            #print(endingPoint)
        if letter.lower() == "u":
            endingPoint[1] = endingPoint[1] + 1
            #print(endingPoint)
        if letter.lower() == "d":
            endingPoint[1] = endingPoint[1] - 1
            #print(endingPoint)

    #print(startingPoint, ":", endingPoint)
    
    if (startingPoint == endingPoint):
        print("Output: True")
        return True
    else:
        print("Output: False")
        return False

def morseCodeConverter():
    word = input("What is your word: ")
    word = word.lower()
    output = ""
    morseCode = [".‐","‐...","‐.‐.","‐..",".","..‐.","‐‐.","....","..",".‐‐‐","‐.‐",".‐..","‐‐","‐.",
"‐‐‐",".‐‐.","‐‐.‐",".‐.","...","‐","..‐","...‐",".‐‐","‐..‐","‐.‐‐","‐‐.."]

    #map each letter of the alphabet to a morse code character
    for letter in word:
        if (letter == 'a'):
            output = output + " " + morseCode[0]
        if (letter == 'b'):
            output = output + " " + morseCode[1]
        if (letter == 'c'):
            output = output + " " + morseCode[2]
        if (letter == 'd'):
            output = output + " " + morseCode[3]
        if (letter == 'e'):
            output = output + " " + morseCode[4]
        if (letter == 'f'):
            output = output + " " + morseCode[5]
        if (letter == 'g'):
            output = output + " " + morseCode[6]
        if (letter == 'h'):
            output = output + " " + morseCode[7]
        if (letter == 'i'):
            output = output + " " + morseCode[8]
        if (letter == 'j'):
            output = output + " " + morseCode[9]
        if (letter == 'k'):
            output = output + " " + morseCode[10]
        if (letter == 'l'):
            output = output + " " + morseCode[11]
        if (letter == 'm'):
            output = output + " " + morseCode[12]
        if (letter == 'n'):
            output = output + " " + morseCode[13]
        if (letter == 'o'):
            output = output + " " + morseCode[14]
        if (letter == 'p'):
            output = output + " " + morseCode[15]
        if (letter == 'q'):
            output = output + " " + morseCode[16]
        if (letter == 'r'):
            output = output + " " + morseCode[17]
        if (letter == 's'):
            output = output + " " + morseCode[18]
        if (letter == 't'):
            output = output + " " + morseCode[19]
        if (letter == 'u'):
            output = output + " " + morseCode[20]
        if (letter == 'v'):
            output = output + " " + morseCode[21]
        if (letter == 'w'):
            output = output + " " + morseCode[22]
        if (letter == 'x'):
            output = output + " " + morseCode[23]
        if (letter == 'y'):
            output = output + " " + morseCode[24]
        if (letter == 'z'):
            output = output + " " + morseCode[25]

    print("Your word in morse code is ", output)

def MakePlural(number, word):
    word = word.lower()
    makePlural = False
    if (number == 0 or number > 1):
        makePlural = True
    if (makePlural == True):
        #check if word is longer then 3 chars to avoid errors, implement rule 1/6
        if(len(word) > 3 and word[-3:] == 'ife'):
            print(number, " ", word[:-3] + "ives")
            return
        if (len(word) > 2):
            if(word[-2:] == 'sh'):
                print(number, " ", word[:-2] + "shes")
                return
            elif (word[-2:] == 'ch'):
                print(number, " ", word[:-2] + "ches")
                return
            elif (word[-2:] == 'us'):
                print(number, " ", word[:-2] + "i")
                return
            elif (word[-2:] == 'ay'):
                print(number, " ", word[:-2] + "ays")
                return
            elif (word[-2:] == 'oy'):
                print(number, " ", word[:-2] + "oys")
                return
            elif (word[-2:] == 'ey'):
                print(number, " ", word[:-2] + "eys")
                return
            elif (word[-2:] == 'uy'):
                print(number, " ", word[:-2] + "uys")
                return
        if (len(word) > 1):
            if (word[-1:] == 'y'):
                print(number, " ", word[:-1] + "ies")
                return
        if(len(word) > 0):
            print(number, " ", word + "s")
            return
    else:
        print(number, " ", word)
        return

def is_prime(number):
    isPrime = True
    count = number-1
    #one and zero are not prime and need to be flagged
    if(number == 1 or number == 0):
        isPrime = False
    while (count > 1):
        #loop through all numbers print shout when you find a divider
        if(number % count == 0):
            print(number, "is divisable by ", count)
            isPrime = False
        count = count - 1

    if(isPrime == True):
        print(number, "is prime")
        return True
    else:
        print(number, "is not prime")
        return False

def snake_case(string):
    word = ""
    for letter in string:
        #if the letter is uppercase add an underscore and convert it to lower else just add the letter
        if (True == letter.isupper()):
            word = word + "_" + letter.lower()
        else:
            word = word + letter

    print(string, "was converted to", word)
    return word

def get_number_input():
    number = ""
    #enter loop while number is not an int or float
    while(isinstance(number, (int)) == False and isinstance(number, float) == False):
        #store number then type cast it to a float, if its not an int or float throws error and restarts the loop
        try:
            number = input("Please enter a number: ")
            number = float(number)
        except ValueError:
            print(number, "is not a number, please try again")

    print("Your number is ", number)
    return number


#problem1()
#problem2()
#problem3()
#problem4(0) #run the code with any int other then 0 to execute the code
#problem5("")
#problem6()
#problem7(0)
#problem8("yourTestStringHere")
#problem9()