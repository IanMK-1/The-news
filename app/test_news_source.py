import unittest
from app.models.news_source import NewsSource

Source = NewsSource.Source


class NewsSourceTest(unittest.TestCase):
    """Test class to test newsSource class"""

    def setUp(self) -> None:
        """Instructions to be run before each test case"""

        self.new_source = Source("County-news", "County news", "Kenya", "Source for the best news", "https://abcnews.go.com")

    def test_instance_of_NewsSource(self):
        """Test if new_source is an instance of class NewsSource"""

        self.assertTrue(isinstance(self.new_source, NewsSource))
