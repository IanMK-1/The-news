from app import app
import urllib.request, json
from app.models.news_source import NewsSource
from app.models.news_article import NewsArticle

# Getting API KEY and configuring it to app.config
api_key = app.config['NEWS_API_KEY']

# Getting the News Source base url and configuring it to app.config
news_source_base_url = app.config['NEWS_API_SOURCE_BASE_URL']

# Getting the News Articles base url and configuring it to app.config
news_article_base_url = app.config['NEWS_API_ARTICLES_BASE_URL']


def obtain_news_sources():
    """Obtains the response from the news sources url"""

    news_sources_url = news_source_base_url.format(api_key)

    with urllib.request.urlopen(news_sources_url) as source_url:
        get_news_source_data = source_url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_sources_result = None

        if get_news_source_response['sources']:
            news_sources_result_list = get_news_source_response['sources']
            news_sources_result = process_sources_result(news_sources_result_list)

    return news_sources_result


def process_sources_result(news_sources_list):
    news_sources_result = []

    for news_sources_items in news_sources_list:
        id = news_sources_items.get('id')
        name = news_sources_items.get('name')
        country = news_sources_items.get('country')
        description = news_sources_items.get('description')
        url = news_sources_items.get('url')

        if id:
            news_sources_instances = NewsSource(id, name, country, description, url)
            news_sources_result.append(news_sources_instances)

    return news_sources_result


def obtain_news_article(source_id):
    news_articles_url = news_article_base_url.format(source_id, api_key)

    with urllib.request.urlopen(news_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)

        news_article = None

        if news_articles_response['articles']:
            news_article_list = news_articles_response['articles']
            news_article = process_articles_result(news_article_list)

    return news_article


def process_articles_result(articles):
    news_article_list = []

    for news_article_response in articles:
        title = news_article_response.get('title')
        urlToImage = news_article_response.get('urlToImage')
        description = news_article_response.get('description')
        publishedAt = news_article_response.get('publishedAt')
        url = news_article_response.get('url')

        if id:
            news_article_instances = NewsArticle(title, urlToImage, description, publishedAt, url)
            news_article_list.append(news_article_instances)

    return news_article_list
