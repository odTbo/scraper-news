from requests_html import HTMLSession
from dotenv import load_dotenv
from datetime import datetime
import smtplib
import os
from constants import *

load_dotenv()


class WikiNews:

    def get_articles(self):
        # FETCH WIKI PAGE
        print("Fetching wiki page...")
        r = self.session.get(url=wiki_url, headers=headers)
        item_list = r.html.find(wiki_css)

        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.text
            links = [f'https://en.wikipedia.org{a.attrs["href"]}' for a in item.find("a")]
            article = {
                "title": title,
                "links": links
            }
            self.articles.append(article)
        print(f"Number of articles: {len(self.articles)}")

