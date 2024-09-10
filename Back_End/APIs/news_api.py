from get_data_func import get_data

API_KEY = "f34ceb18736c407588574af26e63e595"


def get_top_news(country=None, news_provider_url=None, keywords=None):
    """
    Fetches top news for a specific region and filtered by keywords.
    """
    api_url = "https://newsapi.org/v2/top-headlines"
    
    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "apiKey": API_KEY
    }

    if country:
        params["country"] = country

    if keywords:
        params["q"] = keywords

    top_news = get_data(api_url, headers=headers, params=params)
    return top_news

print(get_top_news(country="cn"))


