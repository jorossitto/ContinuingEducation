import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


TIME_SPENT = 'TimeSpent'
AGE = 'Age'
AREA_INCOME = 'AreaIncome'
DAILY_INTERNET_USAGE = 'DailyInternetUsage'
ADHEADLINE = 'AdHeadline'
CITY ='City'
MALE ='Male'
COUNTRY ='Country'
CLICKED = 'Clicked'
TIMESTAMP = 'Timestamp'

data = pd.read_csv('../C_Data/advertising.csv',
                   names = ['TimeSpent', 'Age', 'AreaIncome', 'DailyInternetUsage', 'AdHeadline','City', 'Male',
                            'Country', 'Timestamp','Clicked'],
                   header = 1)

#print(data.head(10))
#print(data.info())

#print(data[data.duplicated() == True])

data.drop_duplicates(inplace=True)

#print(data.duplicated().sum())

#print(data[data['TimeSpent'] == '?'])

#print(data.loc[908])

data[TIME_SPENT] = pd.to_numeric(data[TIME_SPENT])
data[AGE] = pd.to_numeric(data[AGE])

#print(data.isnull().sum())

data[AGE] = data[AGE].fillna(data[AGE].median())
data[TIME_SPENT] = data[TIME_SPENT].fillna(data[TIME_SPENT].mean())

data.dropna(inplace=True)

#print(data.isnull().sum())
#print(data.info())

#data.to_csv('../C_Data/advertising_cleaned.csv', index=False)
#print(data.head(10))

numeric = [TIME_SPENT, AGE, AREA_INCOME, DAILY_INTERNET_USAGE]

#print(data[numeric].describe())

categorical = [ADHEADLINE, CITY, MALE, COUNTRY, CLICKED]

#print(data[categorical].describe(include = ['O']))

#print(pd.crosstab(data[COUNTRY], data[CLICKED]).sort_values(1,0, ascending=False).head(15))

#print(pd.crosstab(index=data[COUNTRY], columns='count').sort_values(['count'], ascending=False).head(10))

data['Timestamp'] = pd.to_datetime(data['Timestamp'])

data['Month'] = data[TIMESTAMP].dt.month

data['Day'] = data[TIMESTAMP].dt.day

data['Hour'] = data[TIMESTAMP].dt.hour

data['Weekday'] = data[TIMESTAMP].dt.dayofweek

data = data.drop([TIMESTAMP], axis = 1)

#print(data.head())
def plotClickedOnAdd():
    data[CLICKED].value_counts().plot(kind = 'bar', figsize=(8,6))

    plt.xlabel('clicked on ad')
    plt.ylabel('count')

    plt.show()

def plotMonthlyData():
    monthly_data = data.groupby(['Month'])[CLICKED].sum()
    monthly_data.plot(figsize=(10,6))
    plt.show()

def plotPeakDaysAndHoursClicked():
    f, ax = plt.subplots(1,2, figsize = (15, 5))
    pd.crosstab(data[CLICKED], data['Hour']).T.plot(ax = ax[0])
    pd.pivot_table(data, index = ['Weekday'], values = [CLICKED], aggfunc = np.sum).plot(kind = 'bar', ax = ax[1])
    plt.show()

#print(data.groupby(CLICKED)[TIME_SPENT,AGE, AREA_INCOME, DAILY_INTERNET_USAGE].mean())

def AgeAndTimeSpentScatterPlot():
    sns.jointplot(x = AGE, y = TIME_SPENT, data = data)
    plt.show()

def CorrelationMatrix():
    fig = plt.figure(figsize=(12,8))
    sns.heatmap(data.corr(), cmap = 'summer', annot = True, vmin = -1, vmax = 1)
    plt.show()

#Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

features = [TIME_SPENT, AGE, AREA_INCOME, DAILY_INTERNET_USAGE, MALE]
x = data[features]
y = data[CLICKED]

model = LogisticRegression(solver='lbfgs')
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2)

#xTrain.shape, yTrain.shape

model.fit(xTrain, yTrain)

yPred = model.predict((xTest))

#print(classification_report(yTest, yPred))

#CorrelationMatrix()
