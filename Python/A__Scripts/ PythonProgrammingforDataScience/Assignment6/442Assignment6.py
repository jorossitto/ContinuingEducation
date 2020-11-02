import sys

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.tree = []
        self.depth = 0
        self.count = 0
        self.branch = []
        for item in data:
            self.space = 2 ** self.depth
            #print("Your space is ", self.space)
            #print("Your count is", self.count)
            #print(self.branch)
            #print("Your item is", item)
            #print(self.branch[self.count-1])
            try:
                self.branch[self.count] = item
            except:
                #self.depth =self.depth + 1
                if(self.branch != []):
                    self.tree.append(self.branch)

                self.branch = []
                for i in range(0, self.space):
                    self.branch.append(sys.maxsize)
                #print("Your branch is ", self.branch)
                self.depth = self.depth + 1
                self.count = 0
                self.branch[self.count] = item
            self.count = self.count + 1
        
        if(self.branch != []):
            self.tree.append(self.branch)

        #self.sumTree()

    def preOrder(self):
        count = 0
        preorder = []
        while(count < self.depth):
            for i in range(0, self.depth):
                try:
                    answer = self.tree[i][count]
                    if(answer != sys.maxsize):
                        #print(answer)
                        preorder.append(answer)
                except:
                    min = 1
            count = count + 1
        print("Preorder Traversal: ", preorder)
                #for j in range(0, 2 ** i):
                #    min = self.tree[i][j]
                #for k in (range(0, 2 ** i)):
                    #compair = self.tree[i][k]
                    #if (min < compair):
                        #print(min, compair)
                        #self.tree[i][j] = compair
                        #self.tree[i][k] = min

    def inOrder(self):
        count = 0
        preorder = []
        while (count < self.depth):
            for i in range(self.depth-1, -1, -1):
                try:
                    #print("I is", i)
                    answer = self.tree[i][count]
                    #print("The answer is", answer)
                    if (answer != sys.maxsize):
                        # print(answer)
                        preorder.append(answer)
                except:
                    min = 1
            count = count + 1
        print("Inorder Traversal: ", preorder)
    def postOrder(self):
        count = 0
        postOrder = []
        #while (count < self.depth):
        for i in range(self.depth-1, -1, -1):
            for j in range(0, 2**self.depth):
                try:
                    #print("I is", i)
                    answer = self.tree[i][j]
                    #print("The answer is", answer)
                    if (answer != sys.maxsize):
                        # print(answer)
                        postOrder.append(answer)
                except:
                    min = 1
                #count = count + 1
        print("Post Order Traversal: ", postOrder)

    def sumTree(self):
        count = 0
        sum = []
        #while (count < self.depth):
        #print(self.tree)
        for j in range(0, self.depth):
            number = ""
            for k in range(self.depth-1, -1, -1):
                try:
                    #while(True):
                        #print(k, j)
                    answer = self.tree[k][j]
                    if (answer != sys.maxsize):
                        # print(answer)
                        number = number + str(answer)
                        #j = j +1
                except:
                    number = number + str(self.tree[0][0])
                    min = 1
                #count = count + 1
            number = number[::-1]
            sum.append(int(number))
        print("Paths taken:", sum)
        totalSum = 0
        for number in sum:
            totalSum = totalSum + number
        print("Sum tree: ", totalSum)

    def displayTree(self):
        currentDepth = self.depth
        for branch in self.tree:
            numberToString = ""
            treeBranches = ""
            firstNumber = True
            for number in branch:
                if(number != sys.maxsize and firstNumber):
                    numberToString = numberToString + " " * currentDepth + str(number)
                    firstNumber = False
                elif (number != sys.maxsize):
                    numberToString = numberToString + "  " + str(number)
            print(numberToString)
            currentDepth = currentDepth - 1
            for character in branch:
                #print("Current Depth", currentDepth)
                if(character != sys.maxsize and currentDepth != 0):
                    treeBranches = treeBranches + " "* currentDepth + "/" + " " + "\\" + " "* currentDepth
            print(treeBranches)

def problem1(data):
    """Your task is to re‐create a binary tree using a pre‐order and in‐order traversal lists provided. You
may need to create a class structure for Tree.
In the end, you need to print the tree content using post‐order tree traversal mechanism.
Those not aware of binary tree and tree traversal may read it using the following hyperlink. """

    print("Problem 1")
    #data = [1,2,3,4,5,6]
    binaryTree = BinaryTree(data)
    binaryTree.preOrder()
    binaryTree.inOrder()
    binaryTree.displayTree()
    binaryTree.postOrder()

    #data = [6,5,4,3,2,1]
    #binaryTree = BinaryTree(data)
def problem2():
    """You are given a 2‐D list. Every list has a dish and the ingredients used in it. Your task is to group
the dishes by ingredients. Include the dish only if it is made by more than 1 ingredient.
Also, the output should be in alphabetical order of the ingredients.
You need to write a function for this task. """
    print("Problem 2")
    Input = [["Salad", "Tomato", "Cucumber", "Lettus", "Sauce"],
             ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
             ["Quesadilla", "Chicken", "Cheese", "Sauce"],
             ["Sandwich", "Lettus", "Bread", "Tomato", "Cheese"]]

    ingrediantList = IngrediantList(Input)
def problem3(strings, patterns):
    """. You are given an array of string and an array of patterns. Your task is to check that for every i
and j, the strings and patterns should be the same i.e.
strings[i] = strings[j] and patterns[i] = patterns[j]
Write a function to return True or False. """
    """Example:
strings = ["Python", "Programming", "Programming"] and patterns = ["x", "y", "y"]
Solution: True
strings = ["Python", "Programming", "Class", “Programming”] and patterns = ["x", "y", "y",”y”]
Solution: False
Explanation:  
In 1st example, strings[2]=strings[3] and patterns[2]=patterns[3] => True
In 2nd example, strings[2] != strings[3] != strings[4] and  
         patterns[2] = patterns[3] = patterns[4]   => False"""

    print("Problem 3")
    PaternFinder(strings, patterns)
    print()

    strings = ["Python", "Programming", "Class", "Programming"]
    patterns = ["x", "y", "y","y"]
    PaternFinder(strings, patterns)
def problem4():
    """Your task is to create a binary Tree of digits from 0 to 9 using user inputs. Then display the tree
    using in‐order traversal.
    Next, your task is to iterate through the tree from the root to the leaf nodes and print the path.
    You also need to sum up all the paths in it, as shown in the example.
    Create appropriate class and functions. 
    Example:  User Inputs #
        1
       / \
      0   4
    / \
    3   1
    Inorder traversal: 3,0,1,1,4
    Paths: 1 ‐> 0 ‐> 3
           1 ‐> 0 ‐> 1
           1 ‐> 4
    Sum of all paths: 103 + 101 + 14 = 218
    Explanation: Path traced would be from root to leaf nodes. Sum is the additions of
    all paths."""
    print("Problem 4")
    stillGoing = True
    userInputs = []
    while(stillGoing):
        number = input("Please enter a number")
        try:
            userInputs.append(int(number))
        except:
            stillGoing = False
            min = 1
        #stillGoing = False
    print("You entered: ", userInputs)
    binaryTree = BinaryTree(userInputs)
    binaryTree.displayTree()
    binaryTree.inOrder()
    binaryTree.sumTree()


class IngrediantList():
    def __init__(self, array):
        self.ingrediantDictionary = dict()
        self.dishes = []
        self.sortedItems = []
        self.ingrediants = []
        for menuItem in array:
            self.dishes.append(menuItem[0])
            #self.sortedItems.append(sorted(menuItem))
        #array = self.sortedItems
        for menuItem in array:
            for ingrediant in menuItem:
                if(ingrediant in self.dishes):
                    continue
                if(ingrediant in self.ingrediantDictionary.keys()):
                    self.ingrediants.append(ingrediant)
                    self.ingrediantDictionary[ingrediant] = self.ingrediantDictionary[ingrediant] + ", " + menuItem[0]
                else:
                    self.ingrediantDictionary[ingrediant] = menuItem[0]
        #print(self.dishes)
        self.ingrediants = sorted(set(self.ingrediants))
        #print(self.ingrediants)
        for key in self.ingrediants:
            if(key in self.ingrediantDictionary.keys()):
                print("Ingrediant:", key, "\t\tUsed for: ", self.ingrediantDictionary[key])
class PaternFinder():
    def __init__(self, strings, patterns):
        print("Strings =", strings, "and patterns =", patterns)
        stringToPatternDict = dict()
        answer = []
        for i in range(0,len(strings)):
            #print(patterns[i])
            stringToPatternDict[patterns[i]] = strings[i]

        for i in range(0, len(strings)):
            #print(stringToPatternDict[patterns[i]])
            answer.append(stringToPatternDict[patterns[i]])

        #print("Answer: ", answer)

        if(answer == strings):
            print("Solution: True")
        else:
            print("Solution: False")
#problem1([1,2,3,4,5,6])
#problem2()
#problem3(strings = ["Python", "Programming", "Programming"], patterns = ["x", "y", "y"])
problem4()