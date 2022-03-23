
from newspaper import Article
import newspaper
import nltk
nltk.download('punkt')

URLS = ['https://www.latimes.com/world-nation/story/2020-09-20/coronavirus-aerosol-airborne-spread',
        'https://edition.cnn.com/2020/12/22/asia/hong-kong-pirates-eli-boggs-intl-hnk-dst/index.html'
        ]


class MainSource(newspaper.Source):
    def __init__(self, articleURL):
        super(MainSource, self).__init__('http://localhost')
        self.articles = [newspaper.Article(url=articleURL)]


sources = [MainSource(articleURL=u) for u in URLS]

newspaper.news_pool.set(sources)
newspaper.news_pool.join()

Final_Summary = ""
for src in sources:
    src.articles[0].download()
    src.articles[0].parse()
    src.articles[0].nlp()
    Final_Summary += src.articles[0].summary + "\n"
    print('Title:', src.articles[0].title)
    print('Author:', src.articles[0].authors)


Final_Summary = Final_Summary[:-1]
print('Summary:', Final_Summary)
