from keys import API_GEOCODE_KEY
from get_data_func import get_data

def get_coordinates(address_to_go):
    """
    gets latitude & longitude for location
    """
    api_url = f"https://api.opencagedata.com/geocode/v1/json?q={address_to_go}&key={API_GEOCODE_KEY}"
    coordinates_to_go = get_data(api_url)

    if coordinates_to_go and coordinates_to_go["results"]:
        first_result = coordinates_to_go["results"][0]
        coordinates = first_result["geometry"]

        if coordinates:
            return coordinates
        else:
            print("No coordinates available")

    return None

