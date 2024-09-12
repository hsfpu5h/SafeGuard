from datetime import datetime, timedelta
from SafeGuard.scripts.keys import API_NEO_KEY
from get_data_func import get_data

def get_neo_data(start_date=None, end_date=None):
    if start_date is None:
        start_date = datetime.now().strftime("%Y-%m-%d")

    if end_date is None:
        end_date_obj = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=3)
        end_date = end_date_obj.strftime("%Y-%m-%d")

    api_url= f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_NEO_KEY}"
    try:
        neo_data = get_data(api_url)
        return neo_data
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None

def get_miss_distance_kilometers():
    neo_data = get_neo_data()
    try:
        distances_kilometers = []
        for date, neos in neo_data["near_earth_objects"].items():
            for neo in neos:
                close_approaches = neo["close_approach_data"]
                for approach in close_approaches:
                    miss_distance = approach["miss_distance"]
                    distance_kilometers = miss_distance["kilometers"]
                    distances_kilometers.append(distance_kilometers)

        return distances_kilometers
    except KeyError as e:
        print(f"KeyError: {e}")
        return None


