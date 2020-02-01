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


def obtain_news_sources(category):
    """Obtains the json response to the news sources url"""

    news_sources_url = news_source_base_url.format(category, api_key)

    with urllib.request.urlopen(news_sources_url) as source_url:
        get_news_source_data = source_url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_sources_result = None

        if get_news_source_response['sources']:
            news_sources_result_list = get_news_source_response['sources']
            news_sources_result = process_sources(news_sources_result_list)

    return news_sources_result
