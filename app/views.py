from flask import render_template,request,redirect,url_for
from app import app
from .request import get_headline,search_country
#from .models import review
#from .forms import ReviewForm
#Review = review.Review

countrylist=['ae', 'ar', 'at' ,'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id','ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']

@app.route('/')
def index():
    """
    root view function

    """
    headlines = get_headline()
    search_input = request.args.get('news_querry')
    business=[] 
    entertainment=[] 
    general=[]
    health=[]
    science=[]
    sports=[]
    technology=[]

    for headline in headlines:
        if headline.category == 'business':
            business.append(headline)
        elif headline.category == 'entertainment':
            entertainment.append(headline)
        
    if search_input:
        return redirect(url_for('search_specific_country',country_name=search_input))
    else:
        return render_template('index.html',headlines =headlines, business=business)


@app.route('/headlines/<headlines>')
def news_details(headlines):
    """
    read full article
search
    """

    return render_template('headlines.html',id = headlines)

@app.route('/search/<country_name>')
def search_specific_country(country_name):


    """
    View function to display country search results

    """
    searched_article_list = search_country(country_name)
    #print(type(searched_article_list))
    return render_template('search.html', articles = searched_article_list)



    