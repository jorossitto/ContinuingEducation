#Description: this program classifies a person as having a cardio vascular disease or not


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from C_Data.configs import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


#load the data
df = pd.read_csv(configs.CARDIO_DATA, sep =';')
print(df.head(7))
print(df.shape)

#Count the empty values
print(df.isna().sum())
print(df.describe())

#get a count of the numbe r of patients with a cardiovascular disease
df['cardio'].value_counts()

#visualize the  count
sns.countplot(df['cardio'])
plt.show()

#look at the number of people with a cardio disease

#create a years column
df['years'] = (df['age']/365).round(0)
df['years'] = pd.to_numeric(df['years'], downcast='integer')

#visualize the data
sns.countplot(x='years', hue='cardio',data=df, palette='colorblind', edgecolor = sns.color_palette('dark',n_colors=1))
plt.show()

#Get the correlation of the columns
print(df.corr())

#visualize the data
plt.figure(figsize= (7,7))
sns.heatmap(df.corr(), annot=True, fmt='.0%')
plt.show()

#remove years
df = df.drop('years', axis=1)

#remove or drop id
df = df.drop('id', axis=1)

#split the data
x = df.iloc[:, :-1].values
y = df.iloc[:,-1].values

#Split the data again, into 75% training and 25% testing data set
xTrain, xTest, yTrain, yTest = train_test_split(x,y, test_size=.2, random_state=1)

#Feature Scaling - scale the values to be between 0 and 1
sc = StandardScaler()
xTrain = sc.fit_transform(xTrain)
xTest = sc.fit_transform(xTest)

#Use Random Forest Classifier
forest = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=1)
forest.fit(xTrain, yTrain)

#Test the model
model = forest
model.score(xTrain, yTrain)
print(model.score(xTrain, yTrain))

#test on the test data
cm = confusion_matrix(yTest, model.predict(xTest))

TrueNegitive = cm[0][0]
TruePositive = cm[1][1]
FalseNegitive = cm[1][0]
FalsePositive = cm[0][1]

print(cm)
print('Model test accuracy = {}'.format((TruePositive+TrueNegitive) /
                                        (TruePositive + TrueNegitive + FalseNegitive + FalsePositive)))
