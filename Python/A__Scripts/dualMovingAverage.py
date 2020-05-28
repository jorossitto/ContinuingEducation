import pandas as pd
import numpy as np
from datetime import  datetime
import BA_DataReader.Stocks as stocks
from C_Data.configs import *

import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

#from google.colab import files
#uploaded = files.upload()

aapl = stocks.Stocks.getQuote('AAPL')
#print (aapl)

#create simple moving average 30 days
SMA30 = pd.DataFrame()
SMA30[configs.ADJ_CLOSE] = aapl[configs.ADJ_CLOSE].rolling(window = 30).mean()
#print(SMA30)

#create simple moving 100 day average
SMA100 = pd.DataFrame()
SMA100[configs.ADJ_CLOSE] = aapl[configs.ADJ_CLOSE].rolling(window = 100).mean()
#print(SMA100)

def quote():
    plt.figure(figsize=(12.5, 4.5))
    plt.plot(aapl[configs.ADJ_CLOSE], label = 'AAPL')
    plt.plot(SMA30[configs.ADJ_CLOSE], label = 'SMA30')
    plt.plot(SMA100[configs.ADJ_CLOSE], label = 'SMA100')
    plt.title('Apple adj close price history')
    plt.xlabel('Dates')
    plt.ylabel('Adj Close Price in USD')
    plt.legend(loc ='upper left')
    plt.show()

#quote()

#create a new dataframe to store all the data
data = pd.DataFrame()
data['AAPL'] = aapl[configs.ADJ_CLOSE]
data['sma30'] = SMA30[configs.ADJ_CLOSE]
data['sma100'] = SMA100[configs.ADJ_CLOSE]

#create a buy and sell signal function
def buySell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['sma30'][i] > data['sma100'][i]:
            if flag !=1:
                sigPriceBuy.append(data['AAPL'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['sma30'][i] < data['sma100'][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data['AAPL'][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

#store the buy and sell data into a variable
buySellData = buySell(data)
data['BuySignalPrice'] = buySellData[0]
data['SellSignalPrice'] = buySellData[1]

#print(data)

plt.figure(figsize=(12.6, 4.6))
plt.plot(data['AAPL'], label = 'AAPL', alpha= 0.35)
plt.plot(data['sma30'], label = 'sma30', alpha= 0.35)
plt.plot(data['sma100'], label = 'sma100', alpha= 0.35)

plt.scatter(data.index, data['BuySignalPrice'], label = 'Buy', marker = '^', color = 'green')
plt.scatter(data.index, data['SellSignalPrice'], label = 'Sell', marker = 'v', color= 'red')
plt.title = ('Apple adjusted close price history buy and sell signals')
plt.xlabel('Dates')
plt.ylabel('Adj close price in usd')
plt.legend(loc='upper left')
plt.show()
