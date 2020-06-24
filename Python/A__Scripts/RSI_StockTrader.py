#Goal: use the RSI value to trade stocks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  BA_DataReader.Stocks import Stocks
from C_Data.configs import *

plt.style.use('fivethirtyeight')

#load the data
fbQuote = Stocks.getQuote('FB')

#show the data
print(fbQuote.head(10))

#Show the price
plt.figure(figsize=(12.2, 4.5))
plt.plot(fbQuote.index, fbQuote[configs.ADJ_CLOSE], label = configs.ADJ_CLOSE)
plt.title(configs.ADJ_CLOSE)
plt.xlabel('Dates' , fontsize = 18)
plt.ylabel('Adj close price usd', fontsize = 18)
plt.show()

#prepare the data to calculate the RSI
#Get the difference in price from the previous day
daysBack = 1
delta = fbQuote[configs.ADJ_CLOSE].diff(daysBack)
delta = delta.dropna()
print(delta.head(10))

#Get the positive gains (up) and negitive gains (down)
up = delta.copy()
down = delta.copy()
up[up < 0] = 0
down[down > 0] = 0

#get the time period
period = 14

#calculate average gain and the average loss
AVGGain = up.rolling(window=period).mean()
AVGLoss = abs(down.rolling(window=period).mean())

#Calculate the RSI
#calculate the RS(relative strength)
relativeStrength = AVGGain / AVGLoss
#Calculate the RSI
RSI = 100 - (100/(1+ relativeStrength))

#show the RSI visually
plt.figure(figsize=(12.2, 4.5))
RSI.plot()
plt.show()

#Create a new DataFrame
RSIData = pd.DataFrame()
RSIData[configs.ADJ_CLOSE] = fbQuote[configs.ADJ_CLOSE]
RSIData['RSI'] = RSI
print(RSIData.head(10))

#Visually Show the Adjusted Close Price and RSI

#Plot the adjusted close price
plt.figure(figsize=(12.2, 4.5))
plt.plot(RSIData.index, RSIData[configs.ADJ_CLOSE])
plt.title(configs.ADJ_CLOSE)
plt.legend(RSIData.columns.values, loc = 'upper left')
plt.show()

#plot the corresponding RSI Values and significatnt levels
plt.figure(figsize=(12.2, 4.5))
plt.title('RSI Plot')
plt.plot(RSIData.index, RSIData['RSI'])
plt.axhline(0, linestyle='--', alpha = .5, color='grey')
plt.axhline(10, linestyle='--', alpha = .5, color='orange')
plt.axhline(20, linestyle='--', alpha = .5, color='green')
plt.axhline(30, linestyle='--', alpha = .5, color='red')
plt.axhline(70, linestyle='--', alpha = .5, color='red')
plt.axhline(80, linestyle='--', alpha = .5, color='green')
plt.axhline(90, linestyle='--', alpha = .5, color='orange')
plt.axhline(100, linestyle='--', alpha = .5, color='grey')
plt.show()

