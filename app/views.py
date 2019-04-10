from flask import render_template
from app import app

@app.route('/')
def index():
    """
    root view function

    """
    return render_template('index.html')
@app.route('/headlines/<headlines>')
def news_details(headlines):
    """
    read full article

    """

    return render_template('headlines.html',id = headlines)
    