from flask import render_template
from app import app

@app.route('/')
def index():
    """
    root view function

    """
    return render_template('index.html')
@app.route('/everything/<everything>')
def news_details(everything):
    """
    read full article

    """

    return render_template('everything.html',id = everything)
    