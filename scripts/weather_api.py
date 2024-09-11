from keys import API_WEATHERAPI_KEY
from get_data_func import get_data

def get_forecast(location_query=None, days=None):
    """
       constructs url to get forecast for certain days (3 default)
       """

    if not days:
        days = 3

    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_WEATHERAPI_KEY}&q={location_query}&days={days}&alerts=yes"
    forecast_data = get_data(api_url)

    return forecast_data