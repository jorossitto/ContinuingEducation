import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from C_Data.configs import *
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

#import Dataset
dataset = pd.read_csv(configs.POSITIONSALARIES)
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

#split the data into the Training set and Test set
#xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=0.2, random_state=1)

#training the linear regression model on the whole data set
linearRegression = LinearRegression()
linearRegression.fit(x,y)

#Training the polynomial regression model on the whole data set
polynomialRegressor = PolynomialFeatures(degree=4)
xPoly = polynomialRegressor.fit_transform(x)
linearRegressionForPolly = LinearRegression()
linearRegressionForPolly.fit(xPoly, y)

#visualising the linear Regression results
plt.scatter(x,y, color = 'red')
plt.plot(x, linearRegression.predict(x), color = 'blue')
plt.title('Predicted Salaries')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()

#visualising the Polynomial Regression results
plt.scatter(x,y, color = 'red')
plt.plot(x, linearRegressionForPolly.predict(xPoly), color = 'blue')
plt.title('Predicted Salaries')
plt.xlabel('Position Level')
plt.ylabel('Salaries')
plt.show()

#predicting a new result with polly
print(linearRegression.predict([[6.5]]))
print(linearRegressionForPolly.predict(polynomialRegressor.fit_transform([[6.5]])))

