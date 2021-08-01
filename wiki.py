from requests_html import HTMLSession
from dotenv import load_dotenv
from datetime import datetime
import smtplib
from variables import *
import os

load_dotenv()


class WikiNews:
    def __init__(self):
        self.from_email = os.getenv("FROM_EMAIL")
        self.to_email = os.getenv("TO_EMAIL")
        self.e_pass = os.getenv("PASSWORD")
        self.articles = []
        self.mail_content = ""
        self.session = HTMLSession()

        self.get_articles()
        self.create_email()
        self.send_email()

    def get_articles(self):
        # FETCH WIKI PAGE
        print("Fetching wiki page...")
        r = self.session.get(url=url, headers=headers)
        item_list = r.html.find(css_selector)

        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.text
            links = [f'https://en.wikipedia.org{a.attrs["href"]}\n' for a in item.find("a")]
            article = {
                "title": title,
                "links": links
            }
            self.articles.append(article)
        print(f"Number of articles: {len(self.articles)}")

    def create_email(self):
        today = datetime.now()
        today = today.strftime("%d/%m/%Y")

        # CREATE EMAIL CONTENT
        print("Creating email...")
        self.mail_content = f"Subject: Wiki News {today}\n\n"
        for a in self.articles:
            self.mail_content += f'\n{a["title"]}\n'
            for link in a["links"]:
                self.mail_content += link

    def send_email(self):
        try:
            print("Sending...")
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                connection.login(user=self.from_email, password=self.e_pass)
                connection.sendmail(
                    from_addr=self.from_email,
                    to_addrs=self.to_email,
                    msg=self.mail_content
                )
        finally:
            print("Done.")


if __name__ == "__main__":
    wiki = WikiNews()