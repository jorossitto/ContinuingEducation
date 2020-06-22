#Get the sentiment of text from a website

from textblob import TextBlob
import nltk
from newspaper import Article

url = 'https://everythingcomputerscience.com'
article = Article(url)

#Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#Get the summary of the article
text = article.summary

#print the text
print(text)

#create a text blob object
textBlob = TextBlob(text)
#returns a value between -1(negitive) and 1(positive)
sentiment = textBlob.sentiment.polarity
print(sentiment)

if sentiment == 0:
    print('The text is neutral')
elif sentiment > 0:
    print('This text is positive')
elif sentiment < 0:
    print('This text is negitive')
else:
    print('Something went wrong when analizing the text and the sentiment is ',sentiment)

