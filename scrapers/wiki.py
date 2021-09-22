from scrapers.constants import *
from requests_html import HTMLSession


class WikiScraper:
    NAME = "WIKI"

    def __init__(self):
        self.session = HTMLSession()

    def get_articles(self) -> list:
        # FETCH WIKI PAGE
        print("Fetching wiki page...")
        r = self.session.get(url=wiki_url, headers=headers)
        item_list = r.html.find(wiki_selector)

        articles = []
        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.text
            links = [f'https://en.wikipedia.org{a.attrs["href"]}' for a in item.find("a")]
            article = {
                "title": title,
                "body": "\n".join(links)
            }
            articles.append(article)

        print(f"Number of articles: {len(articles)}")
        return articles


if __name__ == "__main__":
    s = WikiScraper()
    print(s.get_articles())
