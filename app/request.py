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

        if title:
            article_object = Headline(title,description,content,urlToImage)
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
    search_country_url = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={country,api_key}'

    with urllib.request.urlopen(search_country_url) as url:
        search_country_data = url.read()
        search_country_response = json.loads(search_country_data)

        search_country_results = None

        if search_country_response['articles']:
            search_country_list = search_country_response['articles']
            search_country_results = process_results(search_country_list)


    return search_country_results
