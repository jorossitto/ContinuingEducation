import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
CLOSE = 'Close'


#todo refactor

class Stocks:

    def getQuote(Symbol): #Data Reader
        df = web.DataReader(Symbol, data_source='yahoo', start='2012-01-01', end= datetime.now())
        return df

    def graphClosePriceHistory(data, symbol): #Presentation
        plt.figure(figsize=(16,8))
        plt.title('Close Price History of ' + symbol)
        plt.plot(data[CLOSE])
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price USD ($)')
        plt.show()

    def graphPredictedVSReal(trainedData, predictedData): #Presentation
        plt.figure(figsize=(16,8))
        plt.title('Model')
        plt.xlabel('Date', fontsize = 18)
        plt.ylabel('Close Price USD ($)')
        plt.plot(trainedData[CLOSE])
        plt.plot(predictedData[[CLOSE, 'Predictions']])
        plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
        plt.show()

    def calculateRootMeanSquaredError(predictions, testData): # Logic
        #Closer to 0 the better it is
        rootMeanSquaredError = np.sqrt(np.mean(predictions - testData)**2)
        return rootMeanSquaredError

    def createMLModel(self, xTrain, yTrain):
        #build LSTM Model
        self.model = Sequential()
        self.model.add(LSTM(50, return_sequences=True, input_shape=(xTrain.shape[1],1)))
        self.model.add(LSTM(50, return_sequences=False))
        self.model.add(Dense(25))
        self.model.add(Dense(1))

        #compile the model
        self.model.compile(optimizer='adam', loss='mean_squared_error')

        #Train the model
        self.model.fit(xTrain, yTrain, batch_size=1, epochs=1)
        return self.model

    def machineLearn(self, dataToLearnOn, daysToLookBack, percentOfDataToUseForTraining):
        #create a new dataframe with only the close
        data = dataToLearnOn.filter([CLOSE])

        #convert the dataframe to a numpy array
        dataset = data.values

        #get the number of rows to train the model on 80%
        training_data_len = math.ceil(len(dataset) * percentOfDataToUseForTraining)

        #Scale the data between 0 and 1 for training
        self.scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = self.scaler.fit_transform(dataset)

        #print(scaled_data)

        #Create the training data set
        #scale the training data
        train_data = scaled_data[0:training_data_len, :]

        #split the data into xTrain and yTrain data sets
        xTrain = []
        yTrain =[]

        for i in range(daysToLookBack, len(train_data)):
            xTrain.append(train_data[i-daysToLookBack:i, 0])
            yTrain.append(train_data[i,0])

        #convert xTrain and yTrain to numpy arrays
        xTrain, yTrain = np.array(xTrain), np.array(yTrain)

        #reshape the data
        #print(xTrain.shape)
        xTrain = np.reshape(xTrain, (xTrain.shape[0],xTrain.shape[1],1))

        #Create the ML Model
        Stocks.createMLModel(self, xTrain, yTrain)

        #Create new array containing scaled values from index 1543 to 2003
        test_data = scaled_data[training_data_len - daysToLookBack:,:]

        #create the data sets xTest and yTest
        xTest = []
        yTest = dataset[training_data_len:, :]

        for i in range(daysToLookBack, len(test_data)):
            xTest.append(test_data[i-daysToLookBack:i, 0])

        #convert the data to a numpy array
        xTest = np.array(xTest)

        #Reshape the data
        xTest = np.reshape(xTest, (xTest.shape[0], xTest.shape[1], 1))

        #Get the models predicted price values
        predictions = self.model.predict(xTest)
        predictions = self.scaler.inverse_transform((predictions))

        #Get the root mean squared error (RMSE)
        rootMeanSquaredError = Stocks.calculateRootMeanSquaredError(predictions, yTest)
        print(rootMeanSquaredError)

        #plot the data
        train = data[:training_data_len]
        valid = data[training_data_len:]

        valid['Predictions'] = predictions

        Stocks.graphPredictedVSReal(train, valid)
        print(valid)


