from keys import API_WEATHERAPI_KEY
from get_data_func import get_data

def get_forecast(city, days):
    """
    constructs url to get forecast
        °°°if "alerts=yes" last nested dict is "alerts": {"alert": []}°°°
    """
    api_url = f"http://api.weatherapi.com/v1/forecast.json?key={API_WEATHERAPI_KEY}&q={city}&alerts=yes"
    forecast_data = get_data(api_url)

    if forecast_data:
        return forecast_data
    else:
        print("No data available")