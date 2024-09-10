from keys import API_IQAIR_KEY
from get_data_func import get_data


BASE_URL = "http://api.airvisual.com/v2/"


def get_states_in_country(requested_country):
    """
    gets the available states in a requested_country
    """
    api_url = f"{BASE_URL}states?country={requested_country}&key={API_IQAIR_KEY}"

    headers = {
        "X-Api-Key": API_IQAIR_KEY
    }

    states_in_country = get_data(api_url, headers=headers)
    return states_in_country


def get_cities_in_state(requested_state, requested_country):
    """
        gets available cities in a certain state
    """
    api_url = f"{BASE_URL}cities?state={requested_state}&country={requested_country}&key={API_IQAIR_KEY}"

    headers = {
        "X-Api-Key": API_IQAIR_KEY
    }

    cities_available_data = get_data(api_url, headers=headers)
    return cities_available_data


def get_stations_in_city(requested_city, requested_state, requested_country):
    """
        get different weather stations in requested_city
    """
    api_url = f"{BASE_URL}stations?city={requested_city}&state={requested_state}&country={requested_country}&key={API_IQAIR_KEY}"

    headers = {
        "X-Api-Key": API_IQAIR_KEY
    }

    stations_in_city = get_data(api_url, headers=headers)
    return stations_in_city


def get_air_quality_data(requested_city=None, requested_state=None, requested_country=None, latitude=None, longitude=None):
    """
        gets various data about air quality and weather
    """
    api_url = ""
    if requested_city and requested_state and requested_country:
        api_url = f"{BASE_URL}city?city={requested_city}&state={requested_state}&country={requested_country}&key={API_IQAIR_KEY}"
    elif latitude and longitude:
        api_url = f"{BASE_URL}nearest_city?lat=latitude&lon=longitude&key={API_IQAIR_KEY}"

    headers = {
        "X-Api-Key": API_IQAIR_KEY
    }

    air_quality_data = get_data(api_url, headers=headers)
    return air_quality_data


city="New York City"
state="New York"
country="USA"
#get_stations_in_city(city, state, country)
print(get_cities_in_state(state, country))
#get_air_quality_data(city, state, country)
#get_states_in_country(country)