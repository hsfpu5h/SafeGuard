from required_apis import determine_required_apis
from earthquake_api import get_earthquakes
from geocoding_api import get_coordinates
from global_disaster_api import get_disaster_data
from iqair_api import get_air_quality_data
from neo_api import get_miss_distance_kilometers
from news_api import get_top_news
from tagesschau_api import get_german_news
from weather_api import get_forecast

def fetch_data(location_query=None):
    required_apis = determine_required_apis(location_query)
    results = {}
    for api in required_apis:
        if api == "weather_api":
            results["weather"] = get_forecast(location_query)
        elif api == "tagesschau_api":
            results["german_news"] = get_german_news()
        elif api == "news_api":
            results["news"] = get_top_news(location_query)
        elif api == "neo_api":
            results["events_neo_near_miss"] = get_miss_distance_kilometers() # returns list with near_miss distances
        elif api == "iqair_api":
            results["air_quality"] = get_air_quality_data(location_query)
        elif api == "global_disaster_api":
            results["events_disaster"] = get_disaster_data()
        elif api == "geocoding_api":
            results["coordinates"] = get_coordinates(location_query)
        elif api == "earthquake_api":
            results["events_earthquakes"] = get_earthquakes()
    return results