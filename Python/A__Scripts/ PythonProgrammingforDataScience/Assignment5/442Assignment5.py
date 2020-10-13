import math

class Shape:
    def __init__(self, *args):

        try:
            self.height = args[1]
            self.radius = args[0]
        except:
            self.radius = args[0]
        # write code
        #return super().__init__()

    def Area(self, val):
        area = 0
        #Sphere
        if(val == 'Sphere'):
            area = 4 * math.pi * self.radius ** 2

        # Cyclinder - A=2πrh+2πr2
        if (val == 'Cyclinder'):
            area = 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * 2
        return area

    def Volume(self, val):
        volume = 0
        # sphere
        if (val == 'Sphere'):
            volume = (4/3) * math.pi * self.radius ** 3

        # Cyclinder
        if (val == 'Cyclinder'):
            volume = math.pi * self.radius ** 2 * self.height

        return volume
class Compute:
    """Create a class Compute. Your task is to perform operator overloading. Following are the
operators that would be overloaded.
i. +
The input for the operators would be same sized lists, same sized tuple or variable-sized
dictionary.
Following task needs to be completed:
For + operator, if the caller is a list, then you need to add the contents of the two lists and
return the same sized list. Similarly, you need to add the contents of the two tuples and
return the same sized tuple. For a dictionary, you need to concatenate the two dictionaries. If
the key is already present, then you need to merge the contents or values of those keys. """
    def __init__(self, item):
        self.item = item

    def __add__(self, other):
        listExample = []
        tupleExample = ()
        dictionaryExample = {}
        #print("Starting to add")
        print("Adding ", self.item, " and ", other)
        if (type(other) == type(listExample)):
            for i in range(len(other)):
                #print("Adding ", self.item[i], "+", other[i])
                addedValue = self.item[i] + other[i]
                listExample.append(addedValue)
            return listExample

        #print(type(tupleExample))
        if (type(other) == type(tupleExample)):
            for i in range(len(other)):
                #print("Adding ", self.item[i], "+", other[i])
                addedValue = self.item[i] + other[i]
                listExample.append(addedValue)
            return tuple(listExample)

        #print("Starting dictionaries")
        if (type(other) == type(dictionaryExample)):
            for key in self.item:
                dictionaryExample[key] = self.item[key]
            for key in other:
                if(key in dictionaryExample.keys()):
                    dictionaryExample[key] = dictionaryExample[key] + other[key]
                else:
                    dictionaryExample[key] = other[key]
            return dictionaryExample
class Pathfinder():
    def __init__(self):
        self.inputs = []
        with open("assignment5_input.txt") as file:
            for line in file:
                # remove any extra line breaks
                if (line.isspace() == False):
                    line = line.rstrip('\n')
                    line = line.split(" ")
                    self.inputs.append(line[0])
                    try:
                        self.inputs.append(line[1])
                    except:
                        'do nothing'
        self.matrixSize = int(self.inputs[0])
        self.startLocation = int(self.inputs[1]) - 1
        self.endLocation = int(self.inputs[2]) - 1
        self.area = self.matrixSize * self.matrixSize
        self.matrixContents = []
        #creating the matrix
        for i in range(self.area):
            self.matrixContents.append('-')
        self.matrixContents[self.startLocation] = 'S'
        #print(self.endLocation, "End Location")
        self.matrixContents[self.endLocation] = 'E'

        #creating the obsticals
        for i in range(len(self.inputs)):
            if(i < 3):
                'do nothing'
            else:
                #print("Placing an obstical at ", int(self.inputs[i]) - 1)
                self.matrixContents[int(self.inputs[i]) - 1] = 'O'

    def display(self):
        for i in range(len(self.matrixContents)):
            print(self.matrixContents[i], end=" ")
            mod = (i+1) % self.matrixSize
            #print(mod)
            if(mod == 0):
                print(" ")

    def navigateMaze(self):
        #self.xAxis = self.startLocation / self.matrixSize
        #self.yAxis = self.startLocation % self.matrixSize
        #print(self.startLocation)
        self.currentLocation = self.convertXY(self.startLocation)
        self.XYtoArray(self.currentLocation)
        self.endLocationXY = self.convertXY(self.endLocation)
        finished = False
        step = 0
        while(finished == False):
            if(self.currentLocation[0] > self.endLocationXY[0]):
                step = step + 1
                self.findLeft()
            if (self.currentLocation[0] < self.endLocationXY[0]):
                step = step + 1
                self.findRight()
            if (self.currentLocation[1] < self.endLocationXY[1]):
                step = step + 1
                self.findDown()
            if (self.currentLocation[1] > self.endLocationXY[1]):
                step = step + 1
                self.findUp()
            if(self.currentLocation[0] == self.endLocationXY[0] and self.currentLocation[1] == self.endLocationXY[1]):
                self.matrixContents[self.XYtoArray(self.currentLocation)] = 'E'
                finished = True
            #print("Step ", step)
            if(step > 1000):
                print("Unreachable destination")
                finished = True
        print("Finished =>")
        self.display()
        #print(self.currentLocation)
        
    def convertXY(self, number):
        locationX = number % self.matrixSize
        locationY = int(number / self.matrixSize)
        fullLocation = (locationX, locationY)
        #print(fullLocation)
        return fullLocation

    def XYtoArray(self, xyCord):
        x = xyCord[0]
        y = xyCord[1]
        arrayLocation = (y * self.matrixSize) + x
        #print(arrayLocation)
        return arrayLocation

    def findDown(self):
        try:
            x = self.currentLocation[0]
            y = self.currentLocation[1]
            down = self.XYtoArray((x, y +1))
            if(self.matrixContents[down] != 'O'):
                self.matrixContents[down] = '#'
                #print("Going Down ", self.currentLocation)
                self.currentLocation = (x, y+1)
        except:
            return

    def findUp(self):
        try:
            x = self.currentLocation[0]
            y = self.currentLocation[1]
            up = self.XYtoArray((x, y - 1))
            if (self.matrixContents[up] != 'O'):
                self.matrixContents[up] = '#'
                self.currentLocation = (x, y - 1)
        except:
            return

    def findLeft(self):
        try:
            x = self.currentLocation[0]
            y = self.currentLocation[1]
            left = self.XYtoArray((x -1, y))
            if (self.matrixContents[left] != 'O'):
                self.matrixContents[left] = '#'
                self.currentLocation = (x-1, y)
        except:
            return
    def findRight(self):
        try:
            x = self.currentLocation[0]
            y = self.currentLocation[1]
            Right = self.XYtoArray((x+1, y))
            if (self.matrixContents[Right] != 'O'):
                self.matrixContents[Right] = '#'
                self.currentLocation = (x+1, y)
        except:
            return
class Stack():
    """description of class"""
    def __init__(self, *args, **kwargs):
        # write code
        self.data = []
        for arg in args:
            listArg = [arg]
            self.data = self.data + listArg
        #print(self.data)
        #return super().__init__(*args, **kwargs)
    def push(self, whatToPush):
        # write code
        pushedItem = [whatToPush]
        self.data = self.data + pushedItem
        print("Push Success: ", self.data)
        
    def pop(self):
        # write code
        whatToPop = self.data[0]
        self.data = self.data[1:]
        print("You popped: ", whatToPop)
        print("Pop success current list is: ", self.data)
        return whatToPop

class LinkedList():
    def __init__(self, *args, **kwargs):
        self.tail = None
        self.index = None
        self.addElement(args[0])
        #print(self.tail.letter)
    def addElement(self, elementToAdd):
        newNode = Node(elementToAdd)
        newNode.next = self.tail
        #newNode.previous = self.middle
        self.tail = newNode
        #self.middle = newNode.previous
        print("Adding letter: ", self.tail.letter)
        #print(self.middle.letter)
        #write code
        # Hint: You may need to create a Node class to store the element. Take reference from the already created
        #classes.
        pass

    def removeElement(self, whatToRemove):
        self.index = self.tail
        while(self.index):
            #print(self.index.letter, ":", whatToRemove)
            if(self.index.letter == whatToRemove):
                print("Removing: ", whatToRemove)
                self.index.next = self.index.next.next
            self.index = self.index.next

    def printLinkedList(self):
        #print("Starting to print")
        self.index = self.tail
        printThis = ""
        while(self.index.next != None):
            printThis = printThis + self.index.letter
            self.index = self.index.next
        print("Printing Linked List: ", printThis[::-1])
class Structure(Stack, LinkedList):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
class Node():
    def __init__(self, letter):
        self.letter = letter
        self.next = None
        self.previous = None

def problem1():
    print("Problem 1")
    sphere = Shape(2)  # inputs may change
    print('Sphere area:', sphere.Area('Sphere'))
    print('Sphere volume:', sphere.Volume('Sphere'))
    cyclinder = Shape(1, 2)  # inputs may change
    print('Cyclinder area:', cyclinder.Area('Cyclinder'))
    print('Cyclinder volume:', cyclinder.Volume('Cyclinder'))
def problem2():
    print("Problem 2")
    listOne = [1,2,3,4]
    listTwo = [3.3,4,5,1.2]
    tupleOne = (1, 2, 3, 4)
    tupleTwo = (3.3, 4, 5, 1.2)
    dictionaryOne = {1:'abc',3:'xyz',5:'test'}
    dictionaryTwo = {2:'test1',3:'test2',4:'test3'}

    listOne = Compute([1,2,3,4])
    output = listOne + listTwo
    print(output)

    tupleOne = Compute((1, 2, 3, 4))
    tupleOutput = tupleOne + tupleTwo
    print(tupleOutput)

    dictionaryOne = Compute({1:'abc',3:'xyz',5:'test'})
    dictionaryOutput = dictionaryOne + dictionaryTwo
    print(dictionaryOutput)
def problem3():
    print("Problem 3")
    pathfinder = Pathfinder()
    pathfinder.display()
    pathfinder.navigateMaze()
def problem4():
    """Your task is to perform multiple inheritance. You have two classes, Stack and Linked_List as
the base classes. The Stack base class would have push and pop functions. The Linked_List
would have insert node and delete node functions. The derived class, Structure would call
one of the two classes to perform the function depending on the type of input data.
The Stack class would handle numeric data (int , float , and double) only and Linked_List
class would work on string data.
Do not use any existing libraries for Stack or Linked_List. Also, you cannot use push,
append, pop functions as well. You have to write functions for that. For Linked_List, you
need to create a node and every node would be linked to the next incoming node.
Please note, the code given is an outline for the system to be created. You may need
to make some alterations in the function definitions, etc.
Hint: You may need to create a Node class to store the element. Take reference from
the already created classes. """
    print("Problem 4")
    """
    obj=Structure()
    #input from file
    # if input is numeric
    obj.push()
    #if input is string
    obj.addElement()
    #code to pop element
    obj.pop()
    #code to remove element
    obj.removeElement()
    #print the stack
    #print the linked list
    """
    code = Stack(1,2,3)
    code.push(4)
    code.pop()

    linkedList = LinkedList("")
    linkedList.addElement('s')
    linkedList.addElement('t')
    linkedList.addElement('o')
    linkedList.addElement('p')
    linkedList.printLinkedList()
    linkedList.removeElement('s')
    linkedList.printLinkedList()

#problem1()
#problem2()
#problem3()
problem4()