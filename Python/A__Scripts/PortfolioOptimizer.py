#program attempts to optimize a users portfolio usin gefficient frontier


from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from C_Data.configs import *

from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import DiscreteAllocation, get_latest_prices

tradingDaysPerYear = 252
plt.style.use('fivethirtyeight')

#todo refactor

#assets = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
assets = ["now","cvs","mdwd","vmw","jnce","abbv","cfbk","cmc","met","qrvo","crox","znga","mlnx","alrm","alxn","anet",
"mchp","gms","cs","pcom","nghc","civb","ubcp","nmih","esnt","env","omcl","spns","ssnc","ctxs","prah","bx","cmpr","rop",
"kfy","crmt","pkbk","et","jd","mrcy","lulu","incy","ibp","rh","expe","lfvn","antm","bstc","biib","fbms","tsbk","fbc",
"wal","sbbx","gcbc","ffwm","ubfo","c","akam","azo","ensg","lkq","axe","tecd","pfis","plbc","ew","diod","cag",]

#assign weights to the stocks
#weights = np.array([0.2,0.2,0.2,0.2,0.2])
weights = np.array([0.0]*69)

stockStartDate = '2013-01-01'

today = datetime.today().strftime('%Y-%m-%d')

#create a dataframe to store the adjusted close price of the stocks
df = pd.DataFrame()

#store the adjusted close price into the dataframe
for stock in assets:
    df[stock] = web.DataReader(stock, data_source='yahoo', start = stockStartDate, end = today)[configs.ADJ_CLOSE]

#print(df.head(10))

#Visualize the portfolio
title = 'Portfolio Adj. Close price history'
#get the stocks
myStocks = df

#create and plot the graph
for c in myStocks.columns.values:
    plt.plot(myStocks[c], label = c)

plt.title(title)
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Adj. Price USD', fontsize = 18)
plt.legend(myStocks.columns.values, loc='upper left')
plt.show()

#show the daily simple return
returns = df.pct_change()

#create and show annualized covariance matrix
covMatricAnnual = returns.cov() * tradingDaysPerYear

#print(covMatricAnnual)

#calculate the portfolio variance
portfolioVariance = np.dot(weights.T,np.dot(covMatricAnnual, weights))
#print(portfolioVariance)

#calculate portfolio volitility aka standard deviation
portfolioVolatility = np.sqrt(portfolioVariance)
#print(portfolioVolatility)

#calculate annual portfolio return
portfolioSampleAnnualReturn = np.sum(returns.mean() * weights) * tradingDaysPerYear
#print(portfolioSampleAnnualReturn)

#show the expected annual return, volatility(risk), and variance
percentVariance = str(round(portfolioVariance, 2) * 100) + '%'
percentVolatility = str(round(portfolioVolatility, 2) * 100) + '%'
percentReturn = str(round(portfolioSampleAnnualReturn, 2) * 100) + '%'

print('Expected annual return ' + percentReturn)
print('Expected volitility/risk ' + percentVolatility)
print('Expected variance ' + percentVariance)

#portfolio optimization

#calculate the expected returns and the annualised sample covariance matrix of asset returns
mu = expected_returns.mean_historical_return(df)
sampleCov = risk_models.sample_cov(df)

#optimize for max sharpe ratio
efficientFrontier = EfficientFrontier(mu, sampleCov)

weights = efficientFrontier.max_sharpe()
cleanedWeights = efficientFrontier.clean_weights()
print(cleanedWeights)
efficientFrontier.portfolio_performance(verbose=True)

#get discrete allocation of each share per stock
latestPrices = get_latest_prices(df)
#weights = cleanedWeights
discreteAllocation = DiscreteAllocation(cleanedWeights, latestPrices, total_portfolio_value= 15000 )

allocation, leftover = discreteAllocation.lp_portfolio()
print('Discrete allocation: ', allocation)
print('Funds remaining: ${:2f}'.format(leftover))

