from keys import API_WEATHERAPI_KEY
from get_data_func import get_data

'''def get_forecast(city, days=None):
    """
    constructs url to get forecast for certain days (3 default)
    """
    if not days:
        days = 3

    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_WEATHERAPI_KEY}&q={city}&days={days}&alerts=yes"
    forecast_data = get_data(api_url)

    if forecast_data:
        return forecast_data
    else:
        print("No data available")'''


def get_forecast(location_query=0, days=None):
    """
    Constructs the URL to get the weather forecast for a specific location (city, state, country)
    and for a specified number of days.

    :param city: City name.
    :param state: State name (optional).
    :param country: Country name (optional).
    :param days: Number of days for the forecast (1-10). Default is 3.
    :return: Dictionary containing the forecast data.
    """
    if not days:
        days = 3

    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_WEATHERAPI_KEY}&q={location_query}&days={days}&alerts=yes"
    forecast_data = get_data(api_url)

    return forecast_data