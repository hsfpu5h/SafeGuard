import requests

def get_data(api_url, headers=None, params=None):
    """
    Requests data from a specific URL and returns a dict if the response is JSON.
    """
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error: Response is not valid JSON")

    print(f"Request failed with status code: {response.status_code}")
    return None
'''

def get_data(api_url, params=None):
    """
        requests data from specific url
        returns a dict
    """
    response = requests.get(api_url, params=params)
    print(f"Request URL: {response.url}")  # Debugging: show the full URL being requested
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data
        except Exception as error:
            print(f"Error: {error}")
    else:
        print(f"Failed request: Status code {response.status_code}, Response: {response.text}")
    return None
'''