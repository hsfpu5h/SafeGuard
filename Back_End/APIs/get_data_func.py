import requests

def get_data(api_url, headers=None, params=None):
    """
    Requests data from a specific URL and returns a dict if JSON.
    """
    try:
        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except ValueError:
                print("Error: Response is not valid JSON")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except Exception as e:
        print(f"Request failed: {e}")

    return None

