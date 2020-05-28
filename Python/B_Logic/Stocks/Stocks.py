from BA_DataReader.Stocks import Stocks

symbol = 'NFLX'
df = Stocks.getQuote(symbol)
#print(df)
Stocks.CreatePlotOfStock(df,symbol)
