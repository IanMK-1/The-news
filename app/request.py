from app import app
import urllib.request, json
from app.models.news_source import NewsSource
from app.models.news_article import NewsArticle

# Getting API KEY and configuring it to app.config
api_key = app.config['NEWS_API_KEY']

# Getting the News Source base url and configuring it to app.config
news_source_base_url = app.config['NEWS_API_SOURCE_BASE_URL']

# Getting the News Source base url and configuring it to app.config
news_article_base_url = app.config['NEW_API_ARTICLES_BASE_URL']
