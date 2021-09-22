from abc import ABC, abstractmethod


class ScraperBase:
    NAME = None

    @abstractmethod
    def get_articles(self) -> list:
        pass