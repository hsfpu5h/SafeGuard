from SafeGuard.scripts.keys import API_IQAIR_KEY
from get_data_func import get_data

BASE_URL = "http://api.airvisual.com/v2/"

def get_states_in_country(requested_country):
    """
    gets the available states in a requested_country
    """
    api_url = f"{BASE_URL}states?country={requested_country}&key={API_IQAIR_KEY}"

    states_in_country = get_data(api_url)
    return states_in_country


def get_cities_in_state(requested_state, requested_country):
    """
        gets available cities in a certain state
    """
    api_url = f"{BASE_URL}cities?state={requested_state}&country={requested_country}&key={API_IQAIR_KEY}"

    cities_available_data = get_data(api_url)
    return cities_available_data


def get_stations_in_city(requested_city, requested_state, requested_country):
    """
        get different weather stations in requested_city
    """
    api_url = f"{BASE_URL}stations?city={requested_city}&state={requested_state}&country={requested_country}&key={API_IQAIR_KEY}"

    stations_in_city = get_data(api_url)
    return stations_in_city


def get_air_quality_data(location_query=None, latitude=None, longitude=None):
    """
        gets various data about air quality and weather
    """
    api_url = ""
    if location_query:
        city, state, country = location_query

        query_params = {
            "city": city,
            "state": state,
            "country": country
        }

        query_string = "&".join(f"{key}={value}" for key, value in query_params.items() if value)
        api_url = f"{BASE_URL}city?{query_string}&key={API_IQAIR_KEY}"

    elif latitude and longitude:
        api_url = f"{BASE_URL}nearest_city?lat={latitude}&lon={longitude}&key={API_IQAIR_KEY}"

    air_quality_data = get_data(api_url)
    return air_quality_data
