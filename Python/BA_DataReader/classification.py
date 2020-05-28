import sys
import pandas as pd
import numpy as np
from C_Data.configs import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report


def buildModel (classiferFN, features, label, dataset, testFrac = 0.2): #Logic
    x = dataset[features]
    y = dataset[label]

    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=testFrac)
    model = classiferFN(xTrain, yTrain)

    yPredict = model.predict(xTest)

    print("Features used: ", features)
    summarize_classification(yTest, yPredict) #todo refactor logic can not depend on presentation

    return {'model' : model,
            'xTrain' : xTrain,
            'yTrain' : yTrain,
            'xTest' : xTest,
            'yTest' : yTest,
            'yPredict' : yPredict}

def summarize_classification(yTest, yPredict): #Presentation
    report = classification_report(yTest, yPredict)
    print('Classification report')
    print('--------' * 10)
    print(report)

def logisticFN(xTrain, yTrain, penalty='12', c=1.0, maxIter=1000): #logic
    model = LogisticRegression(penalty=penalty, C=c, max_iter=maxIter, solver='lbfgs')
    model.fit(xTrain, yTrain)
    return model

def decisionTreeFN(xTrain, yTrain, maxDepth=3): #logic
    model = DecisionTreeClassifier(max_depth=maxDepth)
    model.fit(xTrain, yTrain)
    return model
