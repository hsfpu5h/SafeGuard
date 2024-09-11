from SafeGuard.Back_End.APIs.news_api import get_top_news
from tagesschau_api import get_german_news
from weather_api import get_forecast

def fetch_data(required_apis, location_query=None):
    results = {}
    for api in required_apis:
        if api == "weather_api":
            results["weather"] = get_forecast(location_query)
        elif api == "tagesschau_api":
            results["german_news"] = get_german_news()
        elif api == "news_api":
            results["news"] = get_top_news()