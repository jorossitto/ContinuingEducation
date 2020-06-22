from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#Download the punkt package
nltk.download('punkt', quiet=True)

article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()

corpus = article.text
#print(corpus)

#tokenize
text = corpus
sentanceList = nltk.sent_tokenize(text)
#print(sentanceList)

#A function to return a random greeting response to a users greeting
def greetingResponse(text):
    text = text.lower()

    #bots greeting response
    botGreeting = ['howdy', 'hi', 'hey', 'hello', 'hola']
    userGreeting = ['hi', 'hey', 'hello', 'hola', 'greetings']

    for word in text.split():
        if word in userGreeting:
            return random.choice(botGreeting)

def indexSort(inputList):
    length = len(inputList)
    listIndex = list(range(0, length))

    x= inputList
    for i in range(length):
        for j in range(length):
            if x[listIndex[i]] > x[listIndex[j]]:
                temp = listIndex[i]
                listIndex[i] = listIndex[j]
                listIndex[j] = temp
    return listIndex

def BotResponse(userInput):
    userInput = userInput.lower()
    sentanceList.append(userInput)
    botResponse = ''
    countMatrix = CountVectorizer().fit_transform(sentanceList)
    similarityScores = cosine_similarity(countMatrix[-1], countMatrix)
    similarityScoresList = similarityScores.flatten()
    index = indexSort(similarityScoresList)
    #print(similarityScoresList)
    #print(index)
    index = index[1:]
    responseFlag = 0
    j= 0
    for i in range(len(index)):
        if similarityScoresList[index[i]] > 0.0:
            botResponse = botResponse + ' ' + sentanceList[index[i]]
            responseFlag = 1
            j = j+1
        if j > 2:
            break

    if responseFlag == 0:
        botResponse = botResponse + ' ' + "I apologize, I don't understand."
    sentanceList.remove(userInput)
    return botResponse

#Start the chat
print('Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer your queries about chronic kidney disease'
      'if you want to exit, type bye.')
exitList = ['exit', 'see you later', 'bye', 'quit', 'break']

while(True):
    userInput = input()
    if userInput.lower() in exitList:
        print('Doc Bot: chat with you later')
        break
    else:
        if greetingResponse(userInput) != None:
            print('Doc Bot: ' + greetingResponse(userInput))
        else:
            print('Doc Bot: ' + BotResponse(userInput))

BotResponse('hello world')
