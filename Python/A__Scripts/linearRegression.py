import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from C_Data.configs import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#todo Refactor

#import the data
dataset = pd.read_csv(configs.SALARY_DATA)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#split the data
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=.2, random_state=0)

#Training the simple linear regression model on the Training set
regressor = LinearRegression()
regressor.fit(xTrain, yTrain)
linearRegression = LinearRegression(copy_X= True, fit_intercept=True, n_jobs=None, normalize=False)

#predict the test results
yPrediction = regressor.predict(xTest)

#visualize the results
plt.scatter(xTrain, yTrain, color = 'red')
plt.plot(xTrain, regressor.predict(xTrain), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualising the Test set results
plt.scatter(xTest, yTest, color = 'red')
plt.plot(xTrain, regressor.predict(xTrain), color='blue')
plt.title('Salary vs experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#make a prediction
print("In 12 years the salary will be ",regressor.predict([[12]]))#needs 2d array

#getting the final linear regression equasion with the values of coefficients
print("The Coefficient is ",regressor.coef_)
print("The intercept is ",regressor.intercept_)

