from abc import ABC, abstractmethod


class ScraperBase:
    NAME = None

    @abstractmethod
    def get_articles(self) -> list:
        # articles = [{"title": "title_text", "body": "body_text"}, ...]
        # return articles
        pass
