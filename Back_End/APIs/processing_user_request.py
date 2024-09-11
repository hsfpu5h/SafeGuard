'''def get_user_answer(user_data):
    for user in user_data:
        user["city"] = city'''


def get_user_answer(user_data):
    """
    Updates user data by setting the city value from the provided dictionary.

    :param user_data: Dictionary where each key is a user and its value is another dictionary containing user information.
    """
    for user_id, user_info in user_data.items():
        city = user_info.get("city")
        state = user_info.get("state")
        country = user_info.get("country")
        user_info["city"] = city
        user_info["state"] = state
        user_info["country"] = country


# Example usage
user_data = {
    "user1": {"city": "Berlin", "state": "Berlin", "country": "Germany"},
    "user2": {"city": "New York", "state": "NY", "country": "USA"},
}

get_user_answer(user_data)
print(user_data)

