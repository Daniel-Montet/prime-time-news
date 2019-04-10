from flask import render_template
from app import app
from .request import get_headline,search_country

countrylist=['ae', 'ar', 'at' ,'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id','ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
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

@app.route('/search/<country_name>')
def search_specific_country(countryname):


    """
    View function to display country search results

    """
    searched_article_list = search_country(countryname)
    return render_template('search.html',articles = searched_article_list)



    