import os


class Config:
    """Parent configuration class"""

    NEWS_API_SOURCE_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    """Configuration used during production. Inherits from parent class"""
    pass


class DevConfig(Config):
    """Configuration used during development stage"""

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}