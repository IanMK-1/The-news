class Config:
    """Parent configuration class"""

    NEWS_API_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEW_API_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


class ProdConfig(Config):
    """Configuration used during production. Inherits from parent class"""
    pass


class DevConfig(Config):
    """Configuration used during development stage"""

    DEBUG = True
