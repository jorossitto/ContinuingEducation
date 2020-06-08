import numpy as np
from sortedcontainers import SortedList
from B_Logic.MachineLearning.MLPath.util import getData
from datetime import datetime

#todo refactor

class kNeuralNetwork(object):
    def __init__(self, k):
        self.k = k

    def fit(self, x, y):
        self.x = x
        self.y = y

    def predict(self, x):
        y = np.zeros(len(x))
        for i, x in enumerate(x):
            print("K is ... Type", type(self.k))
            sortedList = SortedList([self.k])
            for j, xt in enumerate(self.x):
                diff = x -xt
                d = diff.dot(diff)
                if len(sortedList) < self.k:
                    sortedList.add((d, self.y[j]))
                else:
                    if d < sortedList[-1][0]:
                        del sortedList[-1]
                        sortedList.add((d, self.y[j]))

            votes = {}
            for _, vote in sortedList:
                votes[vote] = votes.get(vote, 0) + 1
            maxVotes = 0
            maxVotesClass = -1
            for vote, count in votes.iteritems():
                if count> maxVotes:
                    maxVotes = count
                    maxVotesClass = vote
            y[i] = maxVotesClass
        return y

    def score(self, x, y):
        prediction = self.predict(x)
        return np.mean(prediction == y)


def main():
    x, y = getData(2000)
    nTrain = 1000
    xTrain, yTrain = x[:nTrain], y[:nTrain]
    xTest, yTest = x[nTrain], y[nTrain]

    for k in (1,2,3,4,5):
        newNetwork = kNeuralNetwork(k)

        t0 = datetime.now()
        newNetwork.fit(xTrain, yTrain)
        print ("Training time:", (datetime.now() - t0))

        t1 = datetime.now()
        print("Train accuracy:", newNetwork.score(xTrain, yTrain))
        print("time to compute train accuracy:", (datetime.now() - t1), "Train size:", len(yTrain))

        t2 = datetime.now()
        print("Test accuracy:", newNetwork.score(xTest, yTest))
        print("time to compute test accuracy:", (datetime.now() - t2), "Train size:", len(yTest))

main()

if __name__ == '__main__':
    x, y = getData(2000)
    nTrain = 1000
    xTrain, yTrain = x[:nTrain], y[:nTrain]
    xTest, yTest = x[nTrain], y[nTrain]
    for k in (1,2,3,4,5):
        kNeuralNetwork = kNeuralNetwork(k)

        t0 = datetime.now()
        kNeuralNetwork.fit(xTrain, yTrain)
        print ("Training time:", (datetime.now() - t0))

        t1 = datetime.now()
        print("Train accuracy:", kNeuralNetwork.score(xTrain), yTrain)
        print("time to compute train accuracy:", (datetime.now() - t1), "Train size:", len(yTrain))

        t2 = datetime.now()
        print("Test accuracy:", kNeuralNetwork.score(xTest), yTest)
        print("time to compute test accuracy:", (datetime.now() - t2), "Train size:", len(yTest))


