from scrapers.constants import *
from requests_html import HTMLSession

regions = [
    "/world/africa",
    "/world/americas",
    "/world/asia-pacific",
    "/world/china",
    "/world/europe",
    "/world/india",
    "/world/middle-east",
    "/world/uk",
    "/world/us",
    # /breakingviews  -not a region
]

categories = [
    "/business/aerospace-defense",
    "/business/autos-transportation",
    "/business/energy",
    "/business/environment",
    "/business/finance",
    "/business/healthcare-pharmaceuticals",
    "/business/media-telecom",
    "/business/retail-consumer",
    "/business/sustainable-business",
    "/business/change-suite",
    "/business/future-of-health",
    "/business/future-of-money",
    "/business/macromatters",
    "/business/take-five",
    "/business/reuters-impact"

]


class ReutersScraper:
    NAME = "REUTERS"

    def __init__(self):
        self.session = HTMLSession()

    def get_articles(self) -> list:
        """Scrapes top articles in the past 24h."""

        print("Fetching Reuters...")
        section = regions[4]
        query = reuters_query(section_id=section)
        r = self.session.get(url=reuters_url, headers=headers, params=query)
        r.raise_for_status()

        content = r.json()["result"]["articles"]

        articles = []
        # # GET ARTICLES
        print("Compiling articles...")
        for article in content:
            title = article["title"]
            link = "https://www.reuters.com" + article["canonical_url"]
            body = article["description"]

            articles.append({
                "title": title,
                "body": body,
                "link": link
            })

        print(f"Number of articles: {len(articles)}")
        return articles


if __name__ == "__main__":
    s = ReutersScraper()
    print(s.get_articles())
    # for category in categories:
    #     print(s.get_articles(category))
