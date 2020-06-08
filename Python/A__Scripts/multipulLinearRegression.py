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

#todo Refactor

#import Dataset
dataset = pd.read_csv(configs.STARTUPS)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(x)
print(y)

columnToOneHotEncode = 3
columnTransformer = ColumnTransformer(transformers=[(configs.ENCODER, OneHotEncoder(), [columnToOneHotEncode])], remainder=configs.PASSTHROUGH)
x = np.array(columnTransformer.fit_transform(x))
print(x)

#split the data into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.2, random_state=1)

#Training the Multiple linear regression model on the training set
regressor = LinearRegression()
regressor.fit(xTrain, yTrain)

#predict the results
yPred = regressor.predict(xTest)
np.set_printoptions(precision=2)
predictedResults = np.concatenate((yPred.reshape(len(yPred), 1), yTest.reshape(len(yTest), 1)),1)
#predictedPercentage = np.array(predictedResults[0]/predictedResults[1])
print(predictedResults)
#print("percentage results ", predictedPercentage)

#Making a single prediction (for example the profit of a startup with R&D Spend = 160000, Administration Spend = 130000,
# Marketing Spend = 300000 and State = 'California')
print("Predicted Profit",regressor.predict([[1,0,0,160000,130000,300000]]))
print("Coef", regressor.coef_)
print("Intercept", regressor.intercept_)
