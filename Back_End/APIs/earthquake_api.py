from get_data_func import get_data

def get_earthquakes(lat=None, lon=None, start_time=None, end_time=None, max_radius_km=None, min_magnitude=None):
    '''
    gets earthquake data for specific parameter & returns dict
    '''
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    params = {
        "format": "geojson",
    }

    if start_time:
        params["starttime"] = start_time
    if end_time:
        params["endtime"] = end_time
    if lat:
        params["latitude"] = lat
    if lon:
        params["longitude"] = lon
    if max_radius_km:
        params["maxradiuskm"] = max_radius_km
    if min_magnitude:
        params["minmagnitude"] = min_magnitude

    earthquake_data = get_data(base_url, params=params)

    if earthquake_data:
        return earthquake_data
    else:
        print("No data available")