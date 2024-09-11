from geocoding_api import get_coordinates

def parse_user_data(user_data):
    """
    parses user data extract location information and retrieve coordinates.
    returns tuple city, state, country and coordinates if available
    """
    location_info = user_data.get("location", {})
    city = location_info.get("city")
    state = location_info.get("state")
    country = location_info.get("country")

    location_query = ", ".join(filter(None, [city, state, country]))

    coordinates = get_coordinates(location_query)

    if not (city or state or country):
        print("No usable data available")

    return location_query, coordinates
