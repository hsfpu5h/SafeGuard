from fetch_api_data import fetch_data

def get_user_answer(user_data):
    """
        processes user_data with apis and returns user_data dict + api_responses
    """
    users_database = {}

    for user_id, user_info in user_data.items():
        city = user_info.get("city")
        state = user_info.get("state")
        country = user_info.get("country")

        location_query = (city, state, country)

        api_responses = fetch_data(location_query)

        users_database[user_id] = {
        "city": city,
        "state": state,
        "country": country,
        "api_responses": api_responses
        }
    return users_database

user_data = {
                "01234": {
                            "city": "Berlin",
                            "state": "Berlin",
                            "country": "Germany"
                        }
                }
#print(get_user_answer(user_data))
