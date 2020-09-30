

def problem1(list):
    """Remove duplicates from a list without the use of any loops, i.e., for, while or if statements.
"""
    print("Problem 1")
    input = [1, 3, 2, 5, 1, 3, 7, 6, 2, 3]
    output = removeDuplicates(input)
    output2 = removeDuplicates(list)

def problem2(list):
    """You are given a matrix, which needs to be horizontally flipped and inverted.
Flipping the matrix horizontally means each row is reversed. Example, row [ 1 0 0 ] would be
flipped to [ 0 0 1 ].
Then you need to invert the matrix i.e., replace 0 by 1 and 1 by 0.
Write a function for the above task. """

    #listReverser([1,1,0])
    #listInverter([1,1,0])
    print("Problem 2")
    reverseThenInvert([[1,1,0],[1,0,1],[0,0,0]] )
    reverseThenInvert(list )

def problem3(input):
    """Every website has subdomains associated with it. Your task is to count the number of hits to
each of the sub-domains.
The input would be like “100 www.facebook.com”, integer and string pair. 100 is the number
of hits to each of the subdomain.
Write a function to accomplish this task.
"""
    print("Problem 3")
    subdomain(input)
    subdomain(["100 www.facebook.com"])
    subdomain(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    #subdomain(["50 yahoo.com"])

def problem4(a, b):
    """You are given two strings, and you need to find the uncommon words. A word is uncommon
if it appears exactly once in one of the strings and does not appear in the other string.
You need to write a function for this task to return a list of uncommon words.
"""
    print("Problem 4")
    uncommonWords("this apple is sweet", "this apple is sour")
    uncommonWords("apple apple", "banana")
    uncommonWords(a, b)

def problem5(inputGrid):
    """You are given a square 2-D array, and each value is termed as the height of each building.
We can increase the height of each building. However, the increase should not exceed the
height of the tallest building in the same row and column.
Write a function to return a new 2-D array that shows the maximum possible heights. Also,
you need to return the total sum of height changes.
"""
    print("Problem 5")
    findGridMax(inputGrid)

def problem6(array):
    """Given an array of strings, group anagrams together. Your task is to write a function to
accomplish this task.
"""
    print("Problem 6")
    anagramFinder(array)
    return

def problem7(array):
    """You are given a sorted array of integers. Every element appears twice except for one
element. Your task is to write a function to find that one element appearing only once in the
array.
Do not use numpy, pandas, dictionary for this question.
Optional Requirement:
Try to write the code for this question with minimal number of lines, i.e. not more than
3-4 lines. """
    print("Problem 7")
    multipleDetector([1, 1, 2, 3, 3, 4, 4, 8, 8])
    multipleDetector([3, 3, 7, 7, 10, 11, 11])
    multipleDetector(array)


def removeDuplicates(list):
    print("Input: ", list)
    list = set(list)
    print(list)
    return list

def listReverser(list):
    newList = []
    count=0
    for number in list[::-1]:
        newList.append(number)

    #print("original: ", list, "reversed list:", newList)
    return(newList)

def listInverter(list):
    newList = []
    for number in list:
        if (number == 0):
            newList.append(1)
        else:
            newList.append(0)
    #print("original: ", list, "inverted list:", newList)
    return(newList)

def reverseThenInvert(list):
    newList = []
    #takes in a larger matrix and parses it into their individual elements then appends the new element to the list
    for element in list:
        element = listReverser(element)
        element = listInverter(element)
        newList.append(element)
    
    print("original list: ", list, "reversed and inverted list:", newList)
    return newList

def subdomain(input):
    domainDictionary = dict()
    #look for all domains inside of the input
    for domain in input:
        subdomainCounter = domain.count('.')
        #split int from domains
        counter = domain.split(" ")
        #set the correct data types for your splits
        counter[1] = str(counter[1])
        counter[0] = int(counter[0])
        firstDomain = counter[1].split(".", 1)
        #try to add more hits to the dictionary, else add the new key to the dictionary
        try:
            domainDictionary[counter[1]] = domainDictionary[counter[1]] + int(counter[0])
        except:
            domainDictionary[counter[1]] = +  int(counter[0])
        secondDomain = firstDomain[1].split(".", 1)
        # try to add more hits to the dictionary, else add the new key to the dictionary
        try:
            domainDictionary[firstDomain[1]] = domainDictionary[firstDomain[1]] + int(counter[0])
        except:
            domainDictionary[firstDomain[1]] =+ counter[0]

        #if there are more then 2 sub domains, continue adding extra keys to the dictionary
        if(subdomainCounter > 1):
            # try to add more hits to the dictionary, else add the new key to the dictionary
            try:
                domainDictionary[secondDomain[1]] = domainDictionary[secondDomain[1]] + int(counter[0])
            except:
                domainDictionary[secondDomain[1]] =+ counter[0]

    print(domainDictionary)

def uncommonWords(a, b):
    print("Input: A =", a, "B =", b)
    firstSentance = a.split()
    secondSentance = b.split()
    finalPhrase = firstSentance + secondSentance
    #print(finalPhrase)
    uncommonWordsList = []
    for word in finalPhrase:
        count = 0
        for item in finalPhrase:
            #print(word, ":", item)
            if (word.lower() != item.lower()):
                count = count + 1
        #count the total words less one because it automatically matches with itself
        totalWords = len(finalPhrase) -1
        #if the two are equal add it to the list because the word is uncommon
        if(count == totalWords):
            uncommonWordsList.append(word)

    print("Output: ", uncommonWordsList)

def findGridMax(grid):
    print(grid)
    columns = []
    columnCount = len(grid)
    highestBuildingColumn = []
    highestBuildingRow = []
    loopCount = 0
    sum = 0

    for row in grid:
        rowMax = 0
        columnMax = 0

        for building in row:
            if (building > rowMax):
                rowMax = building

        column = [column[loopCount] for column in grid]
        for building in column:
            if (building > columnMax):
                columnMax = building

        loopCount = loopCount +1

        highestBuildingRow.append(rowMax)
        highestBuildingColumn.append(columnMax)

    loopCount = 0
    newGrid =[]
    for row in grid:
        columnCount = 0
        newRow = []
        for building in row:
            #print(building)
            if(highestBuildingRow[loopCount] > highestBuildingColumn[columnCount]):
                maxHeight = highestBuildingColumn[columnCount]
            else:
                maxHeight = highestBuildingRow[loopCount]
            if(maxHeight > building):
                sum = sum + (maxHeight - building)
                newRow.append(maxHeight)
            else:
                newRow.append(building)
            columnCount = columnCount +1
        loopCount = loopCount + 1
        newGrid.append(newRow)


    print("The highest building Top to Bottom: ", highestBuildingColumn)
    print("The highest building Left to Right: ", highestBuildingRow)
    #print("Total Columns: ", columnCount, len(grid))
    print("The sum is: ", sum)
    print("The new grid looks like:")
    print(newGrid)

def anagramFinder(array):
    print("Input :", array)
    wordDictionary = dict()
    for word in array:
        #sort the word into a unique dictionary key
        sortedList = sorted(word)
        dictionaryKey = ""
        #loop through the letter array and create the dictionary key
        for letter in sortedList:
            dictionaryKey = dictionaryKey + letter
        #try to add the word to an existing dictionary, if one doesn't exist create a new key page
        try:
            word = word + ", " + wordDictionary[dictionaryKey]
            wordDictionary[dictionaryKey] = word
        except:
            wordDictionary[dictionaryKey] = word

    #for each key print out the words associated with the list
    for key in wordDictionary:
        print(wordDictionary[key])

def multipleDetector(array):
    print("Input: ", array)
    output = []
    for number in array:
        if number in output:
            output.remove(number)
        elif number not in output:
            output.append(number)

    print("Output: ", output)

problem1([1, 3, 2, 5, 1, 3, 7, 6, 2, 3])
#problem2([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
#problem3(["100 www.facebook.com"])
#problem4("your test", "goes here")
#problem5([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
#problem6(["eat", "tea", "tan", "ate", "nat", "bat"])
#problem7([1, 1, 2, 3, 3, 4, 4, 8, 8])