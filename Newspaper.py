
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from textblob import TextBlob
import nltk

nltk.download('punkt')

# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()


url = "https://abcnews.go.com/abcnews/technologyheadlines"
response = requests.get(url)
webpage = response.content
soup = BeautifulSoup(webpage, features='xml')

items = soup.findAll('item')
articles = []
for item in items:
    link = item.find('link').text
    articles.append(link)
    # print(articles)

for url in articles:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # to collect data we need:
    title = article.title
    summary = article.summary
    keywords = article.keywords
    text = article.text
    authors= article.authors
    # image=article.top_image

    # this is to measure sentimentality to determine the tone of the article
    # subjectivity refers to the objectivity of the article
    # polarity refers to the whether a side is being taken and which side an article takes
    text_blob = TextBlob(text)
    polarity_score = text_blob.polarity
    subjectivity_score = text_blob.subjectivity

    print("*******************************")
    print(f"Title: {title}")
    print(f"authors: {authors}")
    print(f"url: {url}")
    print(f"keywords: {keywords}")
    print(f"summary: {summary}")
    print(f"polarity: {polarity_score}")
    print(f"subjectivity: {subjectivity_score}")
    print("*******************************")

# print(response.status_code) should return 200 if uncommented
