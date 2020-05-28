from BA_DataReader.Stocks import Stocks
import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
daysToLookBack = 60
percentageOfData = .8
CLOSE = 'Close'
symbol = 'NFLX'
stocks = Stocks()

df = Stocks.getQuote(symbol)

#print(df)
Stocks.graphClosePriceHistory(df,symbol)

Stocks.machineLearn(stocks, df, daysToLookBack, percentageOfData)

#Get the quote
apple_Quote = web.DataReader('AAPL', data_source='yahoo', start= '2012-01-01', end='2020-05-04')
#Create a new dataframe
newDF = apple_Quote.filter([CLOSE])
#Get the last 60 day closing price values and convert the dataframe to an array
last60Days = newDF[-daysToLookBack:].values

#Scale the data to be values between 0, 1
last60DaysScaled = stocks.scaler.transform(last60Days)

#create an empty list
xTest = []
#append the last 60 days
xTest.append((last60DaysScaled))
#Convert the xTest data set to a numpy array
xTest = np.array(xTest)
#Reshape the data
xTestSamples = xTest.shape[0]
xTestTimeSteps = xTest.shape[1]
xTestFeatures = 1

xTest = np.reshape(xTest,(xTestSamples, xTestTimeSteps, 1))
#Get the predicted scaled price
predictedPrice = stocks.model.predict(xTest)
#undo the scaling
predictedPrice = stocks.scaler.inverse_transform(predictedPrice)
print(predictedPrice)

apple_Quote2 = web.DataReader('AAPL', data_source='yahoo', start= '2020-05-05', end='2020-05-05')
print(apple_Quote2)
