import unittest
from app.models.news_article import NewsArticle


class NewsArticleTest(unittest.TestCase):
    """Test NewsArticleTest tests the NewsArticle class behaviour"""

    def setUp(self) -> None:
        """Instructions to be run before each test case"""

        self.new_article = NewsArticle("Best buys", "https://ichef.bbci.co.uk/images/ic/1024x576/p08121k9.jpg",
                                       "Buy anything you want on best buys", "2020-02-01T11:28:38Z",
                                       "http://www.bbc.co.uk/news/world-51338899")

    def test_instance_of_NewsArticle_class(self):
        self.assertTrue(isinstance(self.new_article, NewsArticle))
