import requests


def get_data(api_url, headers=None, params=None):
    """
    requests data from specific url and returns a dict if json
    """
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Error: Response is not valid JSON")

    print(f"Request failed with status code: {response.status_code}")
    return None