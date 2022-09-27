import pandas as pd
import pymongo

import requests

categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

for list in categories:

    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=' + list + '&'
                                'language=en&'
                                'apiKey=0e97cac02d994073b9a7d649b05e16f7')
    urlResponse = requests.get(url)
    urlResponse = urlResponse.json()

    articles = []
    print(urlResponse)
    try:
        for item in urlResponse['articles']:
            dict = {

                "title": item['title'],
                "urlToImage": item['urlToImage'],
                "description": item['description'],
                "url":item['url']
            }
            articles = articles + [dict]
    except:
        print("Exception occured")

    print(articles)
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    if len(articles) > 0:
        df = pd.DataFrame(urlResponse['articles'])
        df = df.loc[:, ["title", "urlToImage","url"]]
        df.to_csv('Headlines/' + list + '.csv')
