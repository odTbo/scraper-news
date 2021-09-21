from constants import *
from requests_html import HTMLSession


class InterezMixin:
    def __init__(self):
        self.session = HTMLSession()

    def get_article_body(self, link):
        """Scrapes article's body from it's page."""

        # Article page text
        r = self.session.get(link, headers=headers)
        article_page = r.html.find("#clanok", first=True)
        article_text = " ".join([item.text for item in article_page.find("p")])

        return article_text

    def get_articles(self):
        """Scrapes top 4 articles in the past 24h from Interez."""

        print("Fetching Interez...")
        r = self.session.get(url=interez_url, headers=headers)
        item_list = r.html.find(interez_css)

        articles = []
        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.text
            link = item.attrs["href"]
            body = self.get_article_body(link)

            articles.append({
                "title": title,
                "body": body
            })

        print(f"Number of articles: {len(articles)}")
        return articles
        # articles: [{"title": "title_text", "body": "body_text"}, ...]