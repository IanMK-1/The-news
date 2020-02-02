from flask import render_template, url_for
from . import main
from ..request import obtain_news_sources, obtain_news_article


# views
@main.route('/')
def index():
    """Function that returns index page with its data"""

    # Getting the news sources
    all_news_sources = obtain_news_sources()
    # print(all_news_sources)
    return render_template('index.html', news_sources=all_news_sources)


@main.route('/news_articles/<source_id>')
def news_articles(source_id):
    """Function that returns page with articles from a news source"""

    all_articles = obtain_news_article(source_id)

    return render_template('news_articles.html', news_articles=all_articles)
