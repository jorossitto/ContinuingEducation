import numpy as np
import pandas as pd
from C_Data.configs import *

def getData(limit=None):
    print ("reading in and transforming data...")
    df = pd.read_csv(configs.knnTrainingData)
    data = df.as_matrix()
    np.random.shuffle(data)
    x = data[:,1:]/255.0 #data is from 0..255
    y = data[:,0]
    if limit is not None:
        x,y = x[:limit], y[:limit]
    return x,y

def getXor():
    x = np.zeros((200, 2))
    x[:50] = np.random.random((50,2)) / 2 + .5 #(0.5-1, 0.5-1)
    x[50:100] = np.random.random((50,2)) /2
    x[100:150] = np.random.random((50,2)) /2 + np.array([[0,0.5]])
    x[150] = np.random.random((50,2)) / 2 + np.array([[0.5,0]])
    y = np.array([0] * 100 + [1] * 100)
    return x,y

def getDonut():
    n = 200
    rInner = 5
    rOuter = 10
