from flask import render_template
from app import app
from .request import get_headline

@app.route('/')
def index():
    """
    root view function

    """
    headlines = get_headline()
    return render_template('index.html',headlines =headlines)
@app.route('/headlines/<headlines>')
def news_details(headlines):
    """
    read full article

    """

    return render_template('headlines.html',id = headlines)
    