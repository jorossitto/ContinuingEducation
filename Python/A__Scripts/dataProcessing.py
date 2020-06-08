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

#todo Refactor

#import Dataset
dataset = pd.read_csv(configs.EUROPE_DATA)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(x,y)

#take care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print(x)

#encodingthe independent variable
columnTransformer = ColumnTransformer(transformers=[(configs.ENCODER, OneHotEncoder(), [0])], remainder=configs.PASSTHROUGH)
x = np.array(columnTransformer.fit_transform(x))
print(x)

#encoding the dependent Variable
labelEncoder = LabelEncoder()
y = labelEncoder.fit_transform(y)
print(y)

#split the data into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.2, random_state=1)

print(xTrain,'\n\n', xTest, yTrain, yTest)

#Feature Scaling use normalization
standardScaler = StandardScaler()
xTrain[:, 3:] = standardScaler.fit_transform(xTrain[:, 3:])
xTest[:, 3:] = standardScaler.transform(xTest[:, 3:])

print(xTrain)
print(xTest)
