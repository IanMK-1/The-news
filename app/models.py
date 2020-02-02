class NewsArticle:
    """Class NewsArticle creates instances of news articles"""

    def __init__(self, title, urlToImage, description, publishedAt, url):
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        self.url = url


class NewsSource:
    """Class NewsSource creates instances of news sources"""

    def __init__(self, id, name, country, description, url):
        self.id = id
        self.name = name
        self.country = country
        self.description = description
        self.url = url
