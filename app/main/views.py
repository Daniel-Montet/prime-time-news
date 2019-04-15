from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_headline,search_country,get_business_category,get_entertainment_category,get_general_category,get_health_category,get_science_category,get_sports_category,get_technology_category,get_newsid
#from .models import review
#from .forms import ReviewForm
#Review = review.Review

countrylist=['ae', 'ar', 'at' ,'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id','ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']

@main.route('/')
def index():
    """
    root view function

    """
    headlines = get_headline()
    business= get_business_category()
    entertainment= get_entertainment_category()
    general= get_general_category()
    health= get_health_category()
    science= get_science_category()
    sports= get_sports_category()
    technology= get_technology_category()
    search_input = request.args.get('news_querry')
    bbc_news=get_newsid('bbc-news')
    techcrunch=get_newsid('techcrunch')
    business_insider=get_newsid('business-insider')
    abc_news=get_newsid('abc-news')
    al_jazeera_english=get_newsid('al-jazeera-english')
    cnn=get_newsid('cnn')
        
    if search_input:
        return redirect(url_for('search_specific_country',country_name=search_input))
    else:
        return render_template('index.html',headlines =headlines, business=business, entertainment=entertainment, general=general,
        health=health, science=science, sports=sports, technology=technology,bbc_news=bbc_news,techcrunch=techcrunch,business_insider=business_insider
        ,abc_news=abc_news,al_jazeera_english=al_jazeera_english,cnn=cnn)


@main.route('/headlines/<headlines>')
def news_details(headlines):
    """
    read full article
search
    """

    return render_template('headlines.html',id = headlines)

@main.route('/search/<country_name>')
def search_specific_country(country_name):


    """
    View function to display country search results

    """
    searched_article_list = search_country(country_name)
    #print(type(searched_article_list))
    return render_template('search.html', articles = searched_article_list)



    