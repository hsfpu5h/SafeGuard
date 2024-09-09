import os
import requests


API_KEY = os.getenv("API_IQAIR_KEY")
BASE_URL = "http://api.airvisual.com/v2/"


def get_states_in_country(requested_country):
    """
    gets the available states in a requested_country
    """
    api_url = f"{BASE_URL}states?country={requested_country}&key={API_KEY}"
    states_in_country = get_data(api_url)
    return states_in_country


def get_cities_in_state(requested_state, requested_country):
    """
        gets available cities in a certain state
    """
    api_url = f"{BASE_URL}cities?state={requested_state}&country={requested_country}&key={API_KEY}"
    cities_available_data = get_data(api_url)
    return cities_available_data


def get_stations_in_city(requested_city, requested_state, requested_country):
    """
        get different weather stations in requested_city
    """
    api_url = f"{BASE_URL}stations?city={requested_city}&state={requested_state}&country={requested_country}&key={API_KEY}"
    stations_in_city = get_data(api_url)
    return stations_in_city


def get_air_quality_data(requested_city=None, requested_state=None, requested_country=None, latitude=None, longitude=None):
    """
        gets various data about air quality and weather
    """
    api_url = ""
    if requested_city and requested_state and requested_country:
        api_url = f"{BASE_URL}city?city={requested_city}&state={requested_state}&country={requested_country}&key={API_KEY}"
    elif latitude and longitude:
        api_url = f"{BASE_URL}nearest_city?lat=latitude&lon=longitude&key={API_KEY}"
    air_quality_data = get_data(api_url)
    return air_quality_data


def get_data(api_url):
    """
        requests data from specific url
        returns
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print(data)
                return data

        except Exception as error:
            print(f"Error: {error}")
    return None


city="Braunschweig"
state="Lower Saxony"
country="Germany"
#get_stations_in_city(city, state, country)
#get_cities_available(state, country)
#get_air_quality_data(city, state, country)
#get_states_in_country(country)