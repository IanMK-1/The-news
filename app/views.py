from flask import render_template
from app import app
from .request import obtain_news_sources, obtain_news_article


# views
@app.route('/')
def index():
    """Function that returns index page with its data"""

    # Getting the news sources
    all_news_sources = obtain_news_sources()
    # print(all_news_sources)
    return render_template('index.html', news_sources=all_news_sources)


@app.route('/<id>/news_articles')
def news_articles(id):
    """Function that returns page with articles from a news source"""

    articles = obtain_news_article(id)

    render_template('news_articles.html', news_articles=articles)
