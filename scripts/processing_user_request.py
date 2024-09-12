from fetch_api_data import fetch_data

def get_user_answer(user_data):
    """
        processes user_data with apis and returns user_data dict + api_responses
    """
    users_api_responses = {}

    for user_id, user_info in user_data.items():
        city = user_info.get("city")
        state = user_info.get("state")
        country = user_info.get("country")

        location_query = (city, state, country)

        api_responses = fetch_data(location_query)

        users_api_responses[user_id] = {
        "city": city,
        "state": state,
        "country": country,
        "api_responses": api_responses
        }
    return users_api_responses

def parse_api_responses(users_api_responses):
    api_responses = {}

    for user_id, user_info in users_api_responses.items():
        api_responses[user_id] = []

        for response in user_info.get('api_responses', []):
            api_responses[user_id].append(response)

    return api_responses

'''user_data = {
    "01234":    {
        "city": "Berlin",
        "state": "Berlin",
        "country": "Germany"
    }
}'''

