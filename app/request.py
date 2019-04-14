from app import app
import urllib.request,json
from .models import headlines

Headline = headlines.Headline

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]


def process_results(headlines_list):
    """
    Converts the headline result into a list of objects

    Args:
        headlines_list: A list of dictionaries taht contain article details

    Returns:
        headline_results: A list of article objects

    """

    headline_results = []

    for article_item in headlines_list:
        title = article_item.get('title')
        description = article_item.get('description')
        content = article_item.get('content')
        urlToImage= article_item.get('urlToImage')
        url =article_item.get('url')
        category = article_item.get('category')

        if title:
            article_object = Headline(title,description,content,urlToImage,url,category)
            headline_results.append(article_object)

    return headline_results



def get_headline():
    """
    function to get json responce to our url request
    """
    get_headline_url=base_url.format(api_key)

    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)

        headline_results= None

        if get_headline_response['articles']:
            headline_results_list = get_headline_response['articles']

            headline_results = process_results(headline_results_list)

    return headline_results

def search_country(country):
    search_country_url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'.format(country,api_key)

    with urllib.request.urlopen(search_country_url) as url:
        search_country_data = url.read()
        search_country_response = json.loads(search_country_data)

        search_country_results = None

        if search_country_response['articles']:
            search_country_list = search_country_response['articles']
            search_country_results = process_results(search_country_list)


    return search_country_results

def get_business_category():

    business_url = 'https://newsapi.org/v2/top-headlines?category=business&apiKey={}'.format(api_key)

     with urllib.request.urlopen(business_url) as url:
        business_category_data = url.read()
        business_category_response = json.loads(business_category_data)

        business_category_results = None

        if business_category_response['articles']:
            business_category_list = business_category_response['articles']
            business_category_results = process_results(business_category_list)


    return business_category_results

def get_sports_category():

    sports_url = 'https://newsapi.org/v2/top-headlines?category=sports&apiKey={}'.format(api_key)

     with urllib.request.urlopen(sports_url) as url:
        sports_category_data = url.read()
        sports_category_response = json.loads(sports_category_data)

        sports_category_results = None

        if sports_category_response['articles']:
            sports_category_list = sports_category_response['articles']
            sports_category_results = process_results(sports_category_list)


    return sports_category_results

def get_entertainment_category():

    entertainment_url = 'https://newsapi.org/v2/top-headlines?category=entartainment&apiKey={}'.format(api_key)

     with urllib.request.urlopen(entertainment_url) as url:
        entertainment_category_data = url.read()
        entertainment_category_response = json.loads(entertainment_category_data)

        entertainment_category_results = None

        if entertainment_category_response['articles']:
            entertainment_category_list = entertainment_category_response['articles']
            entertainment_category_results = process_results(entertainment_category_list)


    return entertainment_category_results

def get_general_category():

    general_url = 'https://newsapi.org/v2/top-headlines?category=general&apiKey={}'.format(api_key)

     with urllib.request.urlopen(general_url) as url:
        general_category_data = url.read()
        general_category_response = json.loads(general_category_data)

        general_category_results = None

        if general_category_response['articles']:
            general_category_list = general_category_response['articles']
            general_category_results = process_results(general_category_list)


    return general_category_results


def get_health_category():

    health_url = 'https://newsapi.org/v2/top-headlines?category=health&apiKey={}'.format(api_key)

     with urllib.request.urlopen(health_url) as url:
        health_category_data = url.read()
        health_category_response = json.loads(health_category_data)

        health_category_results = None

        if health_category_response['articles']:
            health_category_list = health_category_response['articles']
            health_category_results = process_results(health_category_list)


    return health_category_results

def get_technology_category():

    technology_url = 'https://newsapi.org/v2/top-headlines?category=technology&apiKey={}'.format(api_key)

     with urllib.request.urlopen(technology_url) as url:
        technology_category_data = url.read()
        technology_category_response = json.loads(technology_category_data)

        technology_category_results = None

        if technology_category_response['articles']:
            technology_category_list = technology_category_response['articles']
            technology_category_results = process_results(technology_category_list)


    return technology_category_results

def get_science_category():

    general_url = 'https://newsapi.org/v2/top-headlines?category=general&apiKey={}'.format(api_key)

     with urllib.request.urlopen(general_url) as url:
        general_category_data = url.read()
        general_category_response = json.loads(general_category_data)

        general_category_results = None

        if general_category_response['articles']:
            general_category_list = general_category_response['articles']
            general_category_results = process_results(general_category_list)


    return general_category_results
