#Goal this program classifies images

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from C_Data.configs import *
from skimage.transform import resize

#load the data
from keras.datasets import cifar10

plt.style.use('fivethirtyeight')
(xTrain, yTrain), (xTest, yTest) = cifar10.load_data()


#look at the data types of the variables
print('xtrain Shape: ', xTrain.shape)
print('yTrain Shape: ', yTrain.shape)
print('xTest Shape: ', xTest.shape)
print('xTrain Shape: ', yTest.shape)

#look at the first image as an array
index = 0

#show image as a picture
img = plt.imshow(xTrain[index])
plt.show()

#get the image label
print('The image label is: ', yTrain[index])

#get the image classification
classification = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

#print the image class
print('The Image Class is: ', classification[yTrain[index][0]])

#Convert the labels into a set of 10 numbers to imput into the neural network
yTrainOneHot = to_categorical(yTrain)
yTestOneHot = to_categorical(yTest)

#Print the new label of the image/picture above
print('The one hot label is: ', yTrainOneHot[index])

#Normalize the pixels to be values between 0 and 1
xTrain = xTrain/255
xTest = xTest/255

#Create the models architecture
model = Sequential()

#add the first layer
model.add(Conv2D(32, (5,5), activation='relu', input_shape=(32,32,3)))

#add a pooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#add another layer
model.add(Conv2D(32, (5,5), activation='relu'))

#add a pooling layer
model.add(MaxPooling2D(pool_size=(2,2)))

#add a flattening layer
model.add(Flatten())

#add a layer with 1000 neurons
neurons = 1000
model.add(Dense(neurons, activation='relu'))

#add a dropout layer
model.add(Dropout(0.5))

#add a layer with 500 neurons
neurons = 500
model.add(Dense(neurons, activation='relu'))

#add a dropout layer
model.add(Dropout(0.5))

#add a layer with 250 neurons
neurons = 250
model.add(Dense(neurons, activation='relu'))

#add an output layer with 10 neurons
neurons = 10
model.add(Dense(neurons, activation='softmax'))

#Compile the model
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

#Train the model
hist = model.fit(xTrain, yTrainOneHot, batch_size=256, epochs=10, validation_split= 0.2)

#evaluate the model using the test dataset
evaluation = model.evaluate(xTest, yTestOneHot)[1]
print(evaluation)

#Visualize the models accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='upper left')
plt.show()

#visualize the models loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc='upper right')
plt.show()

catPicture = plt.imread(configs.CATPICTURE)
img = plt.imshow(catPicture)
plt.show()

#resize the image
resizedCatPicture = resize(catPicture, (32,32,3))
plt.imshow(resizedCatPicture)
plt.show()

#Get the model predictions
predictions = model.predict(np.array([resizedCatPicture]))

#show the predictions
print(predictions)

#sort the predictions from least to greatest
listIndex = [0,1,2,3,4,5,6,7,8,9]
x = predictions

for i in range(10):
    for j in range(10):
        if x[0][listIndex[i]] > x[0][listIndex[j]]:
            temp = listIndex[i]
            listIndex[i] = listIndex[j]
            listIndex[j] = temp

#show the sorted labels in order
print(listIndex)

#print the first 5 predictions
for i in range(5):
    print(classification[listIndex[i]], ':', round(predictions[0][listIndex[i]] * 100,2),'%')

