import os
from get_data_func import get_data


API_KEY = os.getenv("API_WEATHERAPI_KEY")
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"


def get_berlin_forecast(city, days):
    '''
    constructs url to get forecast
    '''
    api_url = f"{BASE_URL}?key={API_KEY}&q={city}&days={days}"
    berlin_forecast_data = get_data(api_url)
    return berlin_forecast_data

get_berlin_forecast("Berlin", 3)
