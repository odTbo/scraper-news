from scrapers.constants import *
from requests_html import HTMLSession


class NDTVScraper:
    NAME = "NDTV"

    def __init__(self):
        self.session = HTMLSession()

    # def get_article_body(self, link):
    #     """Scrapes article's body from it's page."""
    #
    #     # Article page text
    #     r = self.session.get(link, headers=headers)
    #
    #     # Article's paragraphs
    #     paragraphs = r.html.find("#clanok > p")
    #
    #     # Text from all paragraph's separated with 2 line breaks
    #     article_text = "<br><br>".join(p.text for p in paragraphs if len(p.text) != 0)
    #
    #     return article_text

    def get_articles(self) -> list:
        """Scrapes top 4 articles in the past 24h from Interez."""

        print("Fetching Interez...")
        r = self.session.get(url=ndtv_url, headers=headers)
        r.raise_for_status()
        item_list = r.html.find(ndtv_selector)
        print(len(item_list))
        print(item_list)
        # articles = []
        # # GET ARTICLES
        # print("Compiling articles...")
        # for item in item_list:
        #     title = item.text
        #     link = item.attrs["href"]
        #     body = self.get_article_body(link)
        #
        #     articles.append({
        #         "title": title,
        #         "body": body
        #     })
        #
        # print(f"Number of articles: {len(articles)}")
        # return articles


if __name__ == "__main__":
    s = NDTVScraper()
    print(s.get_articles())
