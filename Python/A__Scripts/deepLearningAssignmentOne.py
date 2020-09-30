import matplotlib.pyplot as plt
import numpy as np
import glob

import sympy as sym


def ProblemOne():
    x = [1,2,3,4,5,6,7,8,9,10]
    Train(0)
def ProblemTwo():
    learningRate = .01
    x = [1,2,3,4,5,6]
    y = [3.2, 6.4, 10.5, 17.7, 28.1, 38.5]
    MB = RiseOverRun(x, y)
    for item in MB:
        print(*item)
    plt.plot(y)
    plt.show()
def ProblemThree():
    x1 = [1, 1,2,2]
    x2 = [2.2,2.4,2.5,2.7]
    y = [0,1,0,1]
    dataset = [x1, x2, y]
    Nuron(dataset)

def Derivitive(function):
    x = sym.Symbol('x')
    function = function.strip("")
    print(function)
    derivitive = sym.diff(function)
    print(derivitive)

def Nuron(dataset):
    input = dataset[:-1]
    expectedOutput = dataset[-1]
    testData = dataset[:-1]
    Train2(input, expectedOutput)

def Train(input):
    weight = 0.1
    bias = 0.4
    x = input

    for j in range (0, 1000, 1):
        for i in range(1, 10, 1):
            x = i
            expectedOutput = .3 * x + 2
            newWeight = NewWeight(x, weight, bias, expectedOutput)
            newBias = NewBias(x, weight, bias, expectedOutput)
            weight = newWeight
            bias = newBias
            print("weight = ", weight, "bias = ", bias)
    print("weight = ", weight, "bias = ", bias)

def Train2(input, expectedOutput):
    weight = 0.1
    bias = 0.4
    x = input
    for j in range (0, 1000, 1):
        for dataColumn in input:
            count = 0
            for data in dataColumn:
                newWeight = NewWeight(dataColumn[count], weight, bias, expectedOutput[count])
                newBias = NewBias(dataColumn[count], weight, bias, expectedOutput[count])
                weight = newWeight
                bias = newBias
                #print("weight = ", weight, "bias = ", bias)
                count += 1
    print("weight = ", weight, "bias = ", bias)


def NewWeight(x, weight, bias, expectedOutput):
    learningRate = .01
    actualOutput = weight * x + bias
    print("Actual Output: ", actualOutput, " Expected Output: ", expectedOutput)
    gradWeight = -1 * (expectedOutput - actualOutput) * x
    weight = weight - learningRate * gradWeight
    return weight

def NewBias(x, weight, bias, expectedOutput):
    learningRate = .01
    actualOutput = weight * x + bias
    print("Actual Output: ", actualOutput, " Expected Output: ", expectedOutput)
    gradBias = -1 * (expectedOutput - actualOutput) * 1
    bias = bias - learningRate * gradBias
    return bias

def SlopeCalculation(x, y):
    b = None
    m = None

    count = 0
    for number in x:
        if (number == 0):
            b = y[count]
        count += 1

    if (b != None):
        count = 0
        for number in x:
            if(number == 1):
                m = y[count] - b
        count += 1

    if(m != None and b != None):
        return [m, b]

def RiseOverRun(x,y):
    M = []
    B = []
    for number in x[:-1]:
        print(number-1, x[number-1], x[number])
        rise = y[number-1] - y[number]
        run = x[number-1] - x[number]
        m = rise/run
        M.append(m)
        B.append(y[number-1] - m * x[number-1])

    return [M,B]

def ErrorMesurment(expectedOutput, actualOutput, weight, bias):
    error = .5 * (expectedOutput - (weight * actualOutput + bias)) ** 2
    return error

def LeastSquaresRegression():
    #d = 2*5.2 + 4 * 6.7 + 6 * 9.1 + 8 * 10.9
    #print(d)
    #e = 2*5.2 + 2*6.7 +2*9.1 + 2*10.9
    #print(e)
    x = np.ndarray((4,1))
    y = np.ndarray((4,1))
    x[0,0] = 1
    x[1,0] = 2
    x[2,0] = 3
    x[3,0] = 4
    y[0,0] = 5.2
    y[1,0] = 6.7
    y[2,0] = 9.1
    y[3,0] = 10.9
    A = np.ndarray((2,2))
    A[0,0] = 60
    A[0,1] = 20
    A[1,0] = 20
    A[1,1] = 8
    ainv = np.linalg.inv(A)
    z = np.ndarray((2,1))
    z[0,0] = 179
    z[1,0] = 63.8
    res = np.dot(ainv,z) # a = res[0,0] and b=[1,0]
    print(res)

    # do a scatter plot of the data
    area = 10
    colors =['black']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, linewidths=8)
    plt.title('Linear Least Squares Regression')
    plt.xlabel('x')
    plt.ylabel('y')
    #plot the fitted line
    yfitted = x*res[0,0] + res[1,0]
    line,=plt.plot(x, yfitted, '--', linewidth=2) #line plot
    line.set_color('red')
    plt.show()

def LinearLeastSquaresOptimization(y, x, weight, bias, learningRate):
    expectedOutput = y
    for number in expectedOutput-1:
        iteration = number-1
        actualOutput = weight * x[iteration] * bias
        Loss = .5 * (expectedOutput[iteration] - actualOutput) ** 2
        gradWeight = -2 * (Loss) * x[iteration]
        weight[iteration] = weight[iteration] - learningRate * gradWeight
        gradBias = -2 * (Loss)
        bias[iteration] = bias[iteration] - learningRate * gradBias
    return [weight, bias]

#ProblemOne()
#ProblemTwo()
#ProblemThree()

function = "1*x**9"
Derivitive(function)