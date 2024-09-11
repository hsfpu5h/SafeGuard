from keys import API_TOPNEWS_KEY
from get_data_func import get_data

def get_top_news(location_query=None, keywords=None):
    """
    Fetches top news for a specific region and filtered by keywords.
    """
    api_url = "https://newsapi.org/v2/top-headlines"

    params = {
        "apiKey": API_TOPNEWS_KEY
    }

    if location_query:
        city, state, country = location_query

        if country:
            params["country"] = country

    if keywords:
        params["q"] = keywords

    top_news = get_data(api_url, params=params)
    return top_news

#print(get_top_news(None, "Terror"))


