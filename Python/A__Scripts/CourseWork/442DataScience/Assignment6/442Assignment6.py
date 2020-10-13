class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return

class BinaryTree:
    def __init__(self, data):
        self.currentLocation = None
        self.tree = None
        for value in data:
            self.addNode(value)
        print("Init")

        self.nodes = []
        while(self.currentLocation != None):
            for i in range(0, len(data), 3):
                if(i == 0):
                    mainNode = Node(data[i])
                    self.currentLocation = mainNode
                    self.currentLocation.left = Node(data[i+1])
                    self.currentLocation.right = Node(data[i+2])
                elif(i % 2 == 1):
                    self.currentLocation = self.currentLocation.left
                    self.currentLocation = Node(data[i])
                elif(i % 2 == 0):
                    self.currentLocation = self.goRight()
                    self.currentLocation = Node(data[i])
                """
            mainNode.left = 
            mainNode.right = Node(data[i+2])
            mainNode.left.left = No
            print(mainNode.val, " ", mainNode.left.val, " ", mainNode.right.val)"""
    def addNode(self, value):
        if(self.tree == None):
            self.tree = Node(value)
            self.currentLocation = self.tree
            return

        while(self.currentLocation != None):
            self.currentLocation = self.currentLocation.left

        if(self.currentLocation == None):
            self.currentLocation.val = value


    def goLeft(self):
        return self.currentLocation.left
    def goRight(self):
        return self.currentLocation.right
    def printPostOrder(self):
        return
    def __str__(self):
        return

def problem1():
    """Your task is to re‐create a binary tree using a pre‐order and in‐order traversal lists provided. You
may need to create a class structure for Tree.
In the end, you need to print the tree content using post‐order tree traversal mechanism.
Those not aware of binary tree and tree traversal may read it using the following hyperlink. """

    print("Problem 1")
    data = [1,2,3,4,5,6]
    binaryTree = BinaryTree(data)
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
def problem3():
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
        


#problem1()
#problem2()