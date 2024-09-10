import os
from get_data_func import get_data


API_KEY = os.getenv("API_GEOCODE_KEY")


def get_coordinates(address_to_go):
    """
    gets latitude & longitude for location
    """
    api_url = f"https://api.opencagedata.com/geocode/v1/json?q={address_to_go}&key={API_KEY}"
    coordinates_to_go = get_data(api_url)

    if coordinates_to_go and coordinates_to_go['results']:
        first_result = coordinates_to_go['results'][0]
        coordinates = first_result['geometry']
        return coordinates
    return None

