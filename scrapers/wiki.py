from scrapers.constants import *
from requests_html import HTMLSession


class WikiScraper:
    def __init__(self):
        self.session = HTMLSession()

    def get_articles(self):
        # FETCH WIKI PAGE
        print("Fetching wiki page...")
        r = self.session.get(url=wiki_url, headers=headers)
        item_list = r.html.find(wiki_css)

        articles = []
        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.text
            links = [f'https://en.wikipedia.org{a.attrs["href"]}' for a in item.find("a")]
            article = {
                "title": title,
                "links": links
            }
            articles.append(article)

        print(f"Number of articles: {len(articles)}")
        return articles

