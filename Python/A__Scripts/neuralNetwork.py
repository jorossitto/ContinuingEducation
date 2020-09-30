inputs = ""
Synapses = ""
Neuron = ""
Output = ""

import numpy as np
def sigmoid(x):
    return 1/(1 + np.exp(-x))

trainingInputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])
trainingOutputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synapticWeights = 2 * np.random.random((3,1)) - 1
print('Random starting synaptic weights: ')
print(synapticWeights)

for iteration in range(1):
    inputLayer = trainingInputs
    outputs = sigmoid(np.dot(inputLayer, synapticWeights))

print('Outputs after training')
print(outputs)

