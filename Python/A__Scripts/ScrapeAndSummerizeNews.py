#goal this program will scrape and summerize news articles

import nltk
from newspaper import Article

url = 'https://www.npr.org/2020/06/18/880066127/breaking-news-update-supreme-court-rules-against-trump-administration-on-daca'
article = Article(url)

#Do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#get the authors
print(article.authors)

#get the published date
print(article.publish_date)

#get the top image
print(article.top_image)

#get the article text
print(article.text)

#get a summary of the article
print(article.summary)
