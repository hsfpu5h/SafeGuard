from weather_api import get_forecast

def fetch_data(required_apis, city=None, state=None, country=None):
    results = {}
    for api in required_apis:
        if api == "weather_api":
            results["weather"] = get_forecast()
