import requests

def get_data(api_url, params=None):
    """
        requests data from specific url
        returns a dict
    """
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data

        except Exception as error:
            print(f"Error: {error}")
    return None