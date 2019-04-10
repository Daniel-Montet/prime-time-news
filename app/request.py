from app import app
from urllib.request,json
from .models import headlines

Headline = headlines.Headline

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_headline():
    """
    function to get json responce to our url request
    """
    get_headline_url=base_url.format(api_key)

    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data + url.read()
        get_headline_response = json.loads(get_headline_response)

        headline_results= None

        if get_headline_response['articles']:
            headline_results_list = get_headline_response['articles']

            headline_results = process_results(headline_results_list)

    return headline_results