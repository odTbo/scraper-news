from scrapers.constants import *
from requests_html import HTMLSession


class NDTVScraper:
    NAME = "NDTV"

    def __init__(self):
        self.session = HTMLSession()

    def get_article_body(self, link):
        """Scrapes article's body from it's page."""
        def validate(p):
            if len(p.text) == 0:
                return False
            elif "Promoted" in p.text:
                return False
            elif "Except for the headline" in p.text:
                return False
            else:
                return True

        # Article page text
        r = self.session.get(link, headers=headers)

        # Article's paragraphs
        paragraphs = r.html.find(".sp-cn.ins_storybody > p")

        # Text from all paragraphs
        article_text = " ".join(p.text for p in paragraphs if validate(p))

        return article_text

    def get_articles(self) -> list:

        print("Fetching NDTV...")
        r = self.session.get(url=ndtv_url, headers=headers)
        r.raise_for_status()
        item_list = r.html.find(ndtv_selector)
        # print(len(item_list))
        # print(item_list)
        articles = []
        # GET ARTICLES
        print("Compiling articles...")
        for item in item_list:
            title = item.find(".newsHdng", first=True).text
            # link = item.attrs["href"]
            body = item.find("p", first=True).text

            articles.append({
                "title": title,
                "body": body
            })

        print(f"Number of articles: {len(articles)}")
        return articles


if __name__ == "__main__":
    s = NDTVScraper()
    print(s.get_articles())
