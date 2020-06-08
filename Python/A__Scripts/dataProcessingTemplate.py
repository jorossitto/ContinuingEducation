import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from C_Data.configs import *
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

#import Dataset
dataset = pd.read_csv(configs.EUROPE_DATA)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#split the data into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.2, random_state=1)
